class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        # backpack problem

        # states: subset of schemes profit[1..i], rest members j.
        # dp[i][j][k]: number of schemes ending with i, with rest members j, and rest profit k.
        # transition:  dp[i][j][k] = sum_[l in 1..i-1](dp[l][j+group[j]][k+profit[i]]), k > 0
        #              dp[i][j][0] = sum_[l in 1..i-1; m in 0..profit[i]-1](dp[l][j+group[i]][m])
        # boundary: dp[0][G][P] = 1, dp[i][G][k] = 0

        #         dp = [[[0 for _ in range(P+1)] for _ in range(G+1)] for _ in range(len(profit)+1)]
        #         dp[0][-1][-1] = 1

        #         mod = int(1e9+7)
        #         for i in range(1, len(profit)+1):
        #             for j in range(G-group[i-1], -1, -1):
        #                 for k in range(P-profit[i-1], -profit[i-1]-1, -1):
        #                     for l in range(i-1, -1, -1):
        #                         dp[i][j][max(0, k)] = (dp[i][j][max(0, k)] + dp[l][j+group[i-1]][k+profit[i-1]]) % mod

        #         # print(dp)
        #         res = 0
        #         for i in range(1, len(profit)+1):
        #             for j in range(G+1):
        #                 res = (res + dp[i][j][0]) % mod
        #         return res

        # ===================================
        # O(n^4) will cause TLE.

        # change k -> at most rest profit k; i -> for 1..i (not ending at)
        # transition: dp[i][j][k] = dp[i-1][j][k] -> not include profit[i]
        #                           + dp[i-1][j+group[i]][k+profit[i]] -> include profit[i]
        # boundary: dp[i][G][P] = 1, dp[i][G][k] = 0.

        dp = [[[0 for _ in range(P + 1)] for _ in range(G + 1)] for _ in range(len(profit) + 1)]
        dp[0][-1][-1] = 1
        # for i in range(len(profit)+1):
        #     dp[i][-1][-1] = 1

        mod = int(1e9 + 7)
        for i in range(1, len(profit) + 1):
            for j in range(G, -1, -1):
                for k in range(P, -1, -1):
                    dp[i][j][k] = dp[i - 1][j][k]
                for k in range(P, -1, -1):
                    if j + group[i - 1] <= G:  # feasible
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j + group[i - 1]][min(k + profit[i - 1], P)]) % mod

        # print(dp)
        res = 0
        for j in range(G + 1):
            res = (res + dp[-1][j][0]) % mod
        return res
