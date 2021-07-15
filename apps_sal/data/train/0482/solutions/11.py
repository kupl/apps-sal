class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[[0,0] for _1 in range(n)] for _2 in range(n)]
        for i in range(n):
            dp[i][i] = [arr[i], 0] # last number and sum
        for diff in range(1,n):
            for i in range(n-diff): #i,i+1,...,i+diff
                temp_min_ = 10**40
                root = None
                for j in range(i,i+diff):
                    sum_ = (dp[i][j][1] + dp[j+1][i+diff][1]) + dp[i][j][0] * dp[j+1][i+diff][0]
                    if sum_ < temp_min_:
                        temp_min_ = sum_
                        root = max(dp[i][j][0], dp[j+1][i+diff][0])
                dp[i][i+diff] = [root, temp_min_]
                        
        return dp[0][-1][1]
