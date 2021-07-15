class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0]*len(stoneValue)
        for i in range(len(stoneValue)-1, -1, -1):
            ans = float('-inf')
            ans = max(ans, stoneValue[i] - (dp[i+1] if i+1<len(stoneValue) else 0))
            if i+1 < len(stoneValue):
                ans = max(ans, stoneValue[i] + stoneValue[i+1] - (dp[i+2] if i+2 < len(stoneValue) else 0))
            
            if i+2 < len(stoneValue):
                ans = max(ans, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - (dp[i+3] if i+3<len(stoneValue) else 0))
            dp[i]  = ans 
            # num += stoneValue[i] # s[i]
            # ans = max(ans, num-(dp[i+1] if i+1<len(stoneValue) else 0))            
            # # if i+1<len(stoneValue):
            # #     num += stoneValue[i+1] # s[i]+s[i+1]
            # #     ans = max(ans, num-(dp[i+2] if i+2<len(stoneValue) else 0))
            # #     dp[i] = ans
            # # if i+2<len(stoneValue):
            # #     num += stoneValue[i+2] # s[i]+s[i+1]+s[i+2]
            # #     ans = max(ans, num-(dp[i+3] if i+3<len(stoneValue) else 0))
            # #     dp[i] = ans
            # dp[i] = ans

        if dp[0]>0: return 'Alice'
        elif dp[0]<0: return 'Bob'
        else: return 'Tie'
# dp[i] means the difference between the scores of Alice and Bob (relative score the current player can obtain). We want to maximize this difference, in order to make Alice win. Therefore, we traverse the list from the end to the beginning, and calculate this difference as max(s[i]-dp[i+1], s[i]+s[i+1]-dp[i+2], s[i]+s[i+1]+s[i+2]-dp[i+3]). Of course, if any index runs over the boundary of the list, no need to calculate it.


