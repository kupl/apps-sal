from collections import defaultdict
from collections import Counter


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        combo = collections.Counter(x & y for x in A for y in A)

        res = 0
        for a in A:
            for k, v in list(combo.items()):
                if a & k == 0:
                    res += v
        return res
