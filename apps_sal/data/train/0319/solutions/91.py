class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n = len(stoneValue)
        presum = [0] * (n + 1)
        for i, num in enumerate(stoneValue):
            presum[i+1] = presum[i] + num
        presum += [presum[-1]] * 3
        
        dp = [[0] * 2 for _ in range(n+3)]
        for i in range(n-1, -1, -1):
            for k in range(2):
                dp[i][k] = max(-dp[j][1-k] + presum[j] - presum[i] for j in range(i+1, i+4))
        
        if dp[0][0] > 0:
            return 'Alice'
        elif dp[0][0] < 0:
            return 'Bob'
        else:
            return 'Tie'
