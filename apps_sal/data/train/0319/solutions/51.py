from functools import lru_cache


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        minimal = -2 ** 31
        n = len(stoneValue)
        dp = [minimal] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            curr_net = 0
            for j in range(1, min(4, n - i + 1)):
                curr_net += stoneValue[i + j - 1]
                dp[i] = max(dp[i], curr_net - dp[i + j])

        return 'Alice' if dp[0] > 0 else 'Bob' if dp[0] < 0 else 'Tie'
