class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        length = len(stoneValue)
        dp = [0 for _ in range(length + 1)]

        for i in range(length - 1, -1, -1):
            take = 0
            dp[i] = -sys.maxsize
            for j in range(3):
                if i + j < length:
                    take += stoneValue[i + j]
                    dp[i] = max(dp[i], take - dp[i + j + 1])

        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
