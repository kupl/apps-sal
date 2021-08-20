class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n: int = len(stoneValue)
        dp: List[int] = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            taken: int = 0
            for j in range(3):
                if i + j < n:
                    taken += stoneValue[i + j]
                    dp[i] = max(dp[i], taken - dp[i + j + 1])
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
