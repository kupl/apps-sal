class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        M = 10**9 + 7
        cur = [[0]*(G+1) for _ in range(P+1)]
        cur[0][0] = 1
        for p0,g0 in zip(profit,group):
            cur2 = [row[:] for row in cur]
            for p1 in range(P+1):
                p2 = min(p1+p0,P)
                for g1 in range(G-g0+1):
                    g2 = g1+g0
                    cur2[p2][g2] += cur[p1][g1]
                    cur2[p2][g2] %= M
            cur = cur2
        return sum(cur[-1])%M
