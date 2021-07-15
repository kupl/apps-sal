class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * n # max score after i
        dp[-1] = stoneValue[-1]
        dp.append(0)
        for i in range(n-2, -1, -1):
            temp = 0
            for j in range(3):
                if i+j+1>n:
                    break
                temp += stoneValue[i+j]
                dp[i] = max(dp[i], temp-dp[i+j+1])
        if dp[0]>0:
            return 'Alice'
        elif dp[0]<0:
            return 'Bob'
        return 'Tie'

