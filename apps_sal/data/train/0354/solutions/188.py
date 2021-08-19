# [Runtime: 864 ms, faster than 53.84%] DP(bottom-up)
# O(6N * 6T): T: upperbound of rollMax

# f(i, d): number of combinations of res[0~i] if the last number is d
# f(0, ?) = 1
#                 |------------| <= rollMax[d]
#               d'd d d ... d [d]
#               ? d'd d ... d [d]
#               ? ? d'd ... d [d]
#               ? ? ? d'... d [d]
#               ? ? ? ? ... d'[d]
# f(i, d) = sum{ f(j, d') for j in i-rollMax[d] ~ i-1 for d' in 0~5
#               if i-rollMax[d] >= 0 and d' != d }
#          sum{ f(i-1, d') for any d' if i < rollMax[d]} < no limit
# or
# total(i) = sum(f(i, d) for d in range(6))
# f(i, d) = sum( total[j] - f(j, d) for j in i-rollMax[d]~i-1 ) if i >= rollMax[d]
#          total[i-1] if i < rollMax[d]
MOD = 1000000007


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 6 for _ in range(n)]
        total = [0] * n
        for d in range(6):
            dp[0][d] = 1
        total[0] = sum(dp[0][d] for d in range(6))
        for i in range(1, n):
            for d in range(6):
                if i < rollMax[d]:  # no constraint
                    dp[i][d] = total[i - 1]
                else:
                    dp[i][d] = sum(total[j] - dp[j][d] for j in range(i - rollMax[d], i)) % MOD
            total[i] = sum(dp[i][d] for d in range(6)) % MOD
        return total[n - 1]
