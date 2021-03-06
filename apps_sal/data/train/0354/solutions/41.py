class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = collections.deque([[0] * 7 for i in range(max(rollMax))])
        dp[0] = [1] * 7
        for i in range(1, n + 1):
            dp2 = [0] * 7
            for j in range(7):
                for d in range(6):
                    if d == j:
                        continue
                    for k in range(min(rollMax[d], i)):
                        dp2[j] = (dp2[j] + dp[k][d]) % MOD
            dp.pop()
            dp.appendleft(dp2)
        return dp[0][6] % MOD
