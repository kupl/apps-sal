class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        MOD = 10**9 + 7
        cur = [[0] * (G + 1) for _ in range(P + 1)]
        cur[0][0] = 1

        for g0, p0 in zip(group, profit):
            curr = [row[:] for row in cur]
            for p1 in range(P + 1):
                p2 = min(P, p1 + p0)
                for g1 in range(G - g0 + 1):
                    g2 = g1 + g0
                    curr[p2][g2] += cur[p1][g1]
                    curr[p2][g2] %= MOD
            cur = curr
        return sum(cur[-1]) % MOD
