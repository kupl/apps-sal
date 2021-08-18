class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        Mod = 10**9 + 7
        l = len(group)
        f = [[[0] * (G + 1) for i in range(P + 1)] for j in range(2)]
        f[1][0][0] = 1
        for i in range(l):
            f[i % 2] = [j[:] for j in f[(i - 1) % 2]]
            for p in range(P + 1):
                for g in range(G + 1 - group[i]):
                    mp = min(P, profit[i] + p)
                    a, b = i % 2, (i - 1) % 2
                    if g + group[i] <= G:
                        f[a][mp][g + group[i]] = (f[a][mp][g + group[i]] + f[b][p][g]) % Mod
        return sum(f[(l - 1) % 2][-1]) % Mod
        Syn = sorted([(profit[i], group[i]) for i in range(l)])
        s, pre = 0, []
        for p in Syn:
            s += p[0]
            pre.append(s)
        Memo = {}

        def dfs(g, p, i):
            if (g, p, i) in Memo:
                return Memo[g, p, i]
            if i == 0:
                if p <= 0:
                    Memo[g, p, i] = 1
                    if g >= Syn[i][1]:
                        Memo[g, p, i] += 1
                elif p > Syn[i][0]:
                    Memo[g, p, i] = 0
                else:
                    if g >= Syn[i][1]:
                        Memo[g, p, i] = 1
                    else:
                        Memo[g, p, i] = 0
                return Memo[g, p, i]
            if p > pre[i]:
                Memo[g, p, i] = 0
                return 0
            if g == 0 and p <= 0:
                Memo[g, p, i] = 1
                return 1
            if g - Syn[i][1] < 0:
                r = dfs(g, p, i - 1)
            else:
                tmp = p - Syn[i][0] if p - Syn[i][0] >= 0 else 0
                r = (dfs(g - Syn[i][1], p - Syn[i][0], i - 1) + dfs(g, p, i - 1)) % Mod
            Memo[g, p, i] = r
            return r
        dfs(G, P, l - 1)
        return Memo[G, P, l - 1]
