class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        ## https://www.youtube.com/watch?v=WqLslW2sFxU
        n = len(rods)
        if n==0:
            return 0
        sum_ = sum(rods)
        dp = [[-1 for j in range(sum_+1)] for i in range(n+1)]
        dp[0][0] = 0
        for i in range(n+1):
            h = rods[i-1]
            for j in range(sum_-h+1):
                if dp[i-1][j]<0: continue ## invalid state
                ## case 1: not used rods[i-1]
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                ## case 2: add to the taller one
                dp[i][j+h] = max(dp[i][j+h], dp[i-1][j])
                ## case 3: add to the shorter one
                dp[i][abs(j-h)] = max(dp[i][abs(j-h)], dp[i-1][j] + min(h, j))
                
                
#         for i in range(n+1):
#             print(dp[i])
            
        return dp[n][0]
