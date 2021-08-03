class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        stone_sum = 0
        dp = [0] * (len(stoneValue) + 1) + [float('inf')] * 2
        for i in range(len(stoneValue) - 1, -1, -1):
            stone_sum += stoneValue[i]
            chose = min(dp[i + 1], dp[i + 2], dp[i + 3])
            dp[i] = stone_sum - chose
        if dp[i] > stone_sum / 2:
            return 'Alice'
        elif dp[i] < stone_sum / 2:
            return 'Bob'
        else:
            return 'Tie'
