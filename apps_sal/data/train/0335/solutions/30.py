from collections import defaultdict


class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        d = defaultdict(int)
        d[0] = 0
        for i in rods:
            for (sub, b) in list(d.items()):
                d[sub + i] = max(d[sub + i], b + i)
                d[sub - i] = max(d[sub - i], b)
        return d[0]
