from functools import lru_cache
from itertools import combinations


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        val2idx = {v: i for i, v in enumerate(A)}
        
        @lru_cache(None)
        def longest_fib_with_first_second(first, second):
            third = val2idx.get(A[first] + A[second], None)
            if third:
                return 1 + longest_fib_with_first_second(second, third)
            return 2

        ret = max(
            longest_fib_with_first_second(i, j)
            for i, j in combinations(list(range(len(A))), 2)
        )
        return ret if ret >= 3 else 0

