class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        M = pow(10, 9) + 7

        dp = [[0] * (P + 1) for _ in range(G + 1)]
        dp[0][0] = 1

        for k in range(len(group)):
            gro = group[k]
            pro = profit[k]

            for i in range(G - gro, -1, -1):
                for j in range(P, -1, -1):
                    g = i + gro
                    p = min(P, j + pro)
                    dp[g][p] += dp[i][j]

        res = 0
        for i in range(G + 1):
            res += dp[i][P]
        return res % M
