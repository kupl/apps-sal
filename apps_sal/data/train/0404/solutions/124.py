from itertools import combinations
from functools import lru_cache


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        def mean(A):
            return sum(A) / len(A)

        @lru_cache(None)
        def recurse(start, end, k=1):
            if(k == K):
                return mean(A[start:end])
            if(len(A) == 1):
                return A[0]
            maxval = 0
            for i in range(start + 1, end):
                maxval = max(maxval, mean(A[start:i]) + recurse(i, end, k + 1))
            return maxval

        N = len(A)
        return recurse(0, N)
