class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        d = defaultdict(lambda: -math.inf)
        d[0] = 0
        for r in rods:
            e = d.copy()
            for h in list(e.keys())[:]:
                (d[h + r], d[abs(h - r)]) = (max(e[h + 2 * r] + r, e[h + r], e[h] + r), max(e[abs(h - r)], e[h] + r, e[abs(abs(h - r) - r)] + r))
        return d[0] // 2
