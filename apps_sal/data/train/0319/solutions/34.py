class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)
        dp = [float('-inf')] * n
        dp[-1] = stoneValue[-1]
        for i in range(n - 2, -1, -1):
            s = 0
            for j in range(i, i + 3):
                s += stoneValue[j] if j < n else 0
                nxt = dp[j + 1] if j + 1 < n else 0
                dp[i] = max(dp[i], s - nxt)

        ans = dp[0]
        if ans > 0:
            return 'Alice'
        elif ans < 0:
            return 'Bob'
        else:
            return 'Tie'
