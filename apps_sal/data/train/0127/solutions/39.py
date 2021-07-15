class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        # gp = sorted(zip(group, profit))
        gp = list(zip(group, profit))
        # print(gp)
        dp = defaultdict(int)
        dp[(G, P)] = 1
        while gp:
            g, p = gp.pop()
            for (g0, p0), count in list(dp.items()):
                if g0 >= g:
                    prof_left = max(0, p0 - p)
                    dp[(g0 - g, prof_left)] += count
            # print(g, p)
            # print(dp)
        return sum([count for (g, p), count in list(dp.items()) if p == 0]) % ((10 ** 9) + 7)
                    

