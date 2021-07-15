from collections import defaultdict


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        pairs = defaultdict(int)
        for a in A:
            for b in A:
                pairs[a & b] += 1
        res = 0
        for a in A:
            for p, cnt in pairs.items():
                if not a & p:
                    res += cnt
        return res
