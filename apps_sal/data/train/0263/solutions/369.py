class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [0 for i in range(12)]
        num = [1,2,3,4,5,6,7,8,9,11]
        for j in num:
            dp[j] = 1
        for i in range(1,n):
            temp = [0 for l in range(12)]
            for j in num:
                if(j%3==0):
                    temp[j] += dp[j+5] if j+5 in num else 0
                    temp[j] += dp[j-5] if j-5 in num else 0
                    temp[j] += dp[j+1] if j+1 in num else 0
                    temp[j] += dp[j-7] if j-7 in num else 0
                elif(j%3==1):
                    temp[j] += dp[j+5] if j+5 in num else 0
                    temp[j] += dp[j-5] if j-5 in num else 0
                    temp[j] += dp[j+7] if j+7 in num else 0
                    temp[j] += dp[j-1] if j-1 in num else 0
                else:
                    temp[j] += dp[j+5] if j+5 in num else 0
                    temp[j] += dp[j-5] if j-5 in num else 0
                    temp[j] += dp[j+7] if j+7 in num else 0
                    temp[j] += dp[j-7] if j-7 in num else 0
            dp = temp
        return sum(dp)%(10**9+7)
