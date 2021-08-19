from collections import defaultdict


class Solution:

    def countTriplets(self, A: List[int]) -> int:
        d = defaultdict(int)
        mask = (1 << 16) - 1
        for i in A:
            high = mask ^ i
            j = high
            while j:
                d[j] += 1
                j = j - 1 & high
            d[0] += 1
        res = 0
        for i in A:
            for j in A:
                res += d[i & j]
        return res
