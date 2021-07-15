class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        stoneValue.insert(0, 0)
        # dp[i] means the max score we can get when i piles have been taken
        dp = [-sys.maxsize] * (n + 1)
        
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + stoneValue[i]
        
        dp[n] = 0
        for i in reversed(range(n)):
            temp = 0
            for j in range(1, 4):
                if i + j > n:
                    break
                
                temp += stoneValue[i + j]
                dp[i] = max(dp[i], temp + presum[n] - presum[i + j] - dp[i + j])
        
        if dp[0] > presum[n] - dp[0]:
            return 'Alice'
        elif dp[0] < presum[n] - dp[0]:
            return 'Bob'
        else:
            return 'Tie'
