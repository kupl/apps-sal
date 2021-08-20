from collections import Counter
from functools import lru_cache
from itertools import product


class Solution:

    def countTriplets(self, A: List[int]) -> int:

        @lru_cache(None)
        def count_and_zero(x):
            return sum((1 for a in A if a & x == 0))
        pair_and_count = Counter((x & y for (x, y) in product(A, A)))
        return sum((count_and_zero(x) * cnt for (x, cnt) in list(pair_and_count.items())))
