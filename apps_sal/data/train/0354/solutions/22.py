# [] DP(bottom-up)
# O(6N * 6T): T: upperbound of rollMax

# f(i, d): number of combinations of res[0~i] if the last number is d
# f(i, ?) = 1 if i == 0
#                 |------------| <= rollMax[d]
#               d'd d d ... d [d]
#               ? d'd d ... d [d]
#               ? ? d'd ... d [d]
#               ? ? ? d'... d [d]
#               ? ? ? ? ... d'[d]
# f(i, d) = sum{ f(j, d') for j in i-rollMax[d] ~ i-1 for d' in 0~5
#               if i-rollMax[d] >= 0 and d' != d }
#          sum{ f(i-1, d') for any d' if i < rollMax[d]} < no limit
MOD = 1000000007


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 6 for _ in range(n)]
        for d in range(6):
            dp[0][d] = 1
        for i in range(1, n):
            for d in range(6):
                if i < rollMax[d]:  # no constraint
                    dp[i][d] = sum(dp[i - 1][x] for x in range(6)) % MOD
                else:
                    dp[i][d] = sum(dp[j][x] for j in range(i - rollMax[d], i) for x in range(6) if x != d) % MOD
        return sum(dp[n - 1][d] for d in range(6)) % MOD
