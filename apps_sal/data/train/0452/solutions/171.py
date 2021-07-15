class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        
        dp = [[0] * (len(jobDifficulty)) for _ in range(d)]
        
        dp[0][0] = jobDifficulty[0]
        for i in range(1,len(jobDifficulty)):
            dp[0][i] = max(dp[0][i-1], jobDifficulty[i])

        for di in range(1, d):
            for j in range(di, len(jobDifficulty)):
                localMax = jobDifficulty[j];
                dp[di][j] = 10*1000 + 1;
                for r in range(j, di-1, -1):
                    localMax = max(localMax, jobDifficulty[r]);
                    dp[di][j] =  min(dp[di][j], dp[di-1][r-1] + localMax);
                #dp[di][j] = jobDifficulty[j - 1] + dp[di - 1][j-1]
        return dp[-1][-1]
    
    #int localMax = jobDifficulty[j];
    #            dp[i][j] = Integer.MAX_VALUE;
    #            for(int r = j; r >= i; r--){
    #                localMax = Math.max(localMax,jobDifficulty[r]);
    #                dp[i][j] =  Math.min(dp[i][j],dp[i-1][r-1] + localMax);
    #            }class Solution {
    #public int minDifficulty(int[] jobDifficulty, int d) {
        
#\t\tint n = jobDifficulty.length; 
 #       if(n < d) return -1;
#        int[][] dp = new int[d][n];
#        
#        dp[0][0] = jobDifficulty[0];
#        for(int i = 1; i < n; i++){
#            dp[0][i] = Math.max(jobDifficulty[i],dp[0][i-1]);
#        }
        
#        for(int i = 1; i < d; i++){
#            for(int j = i; j < n; j++){
#                int localMax = jobDifficulty[j];
#                dp[i][j] = Integer.MAX_VALUE;
#                for(int r = j; r >= i; r--){
#                    localMax = Math.max(localMax,jobDifficulty[r]);
#                    dp[i][j] =  Math.min(dp[i][j],dp[i-1][r-1] + localMax);
#                }
#            }
#        }
        
#        return dp[d-1][n-1];
#    }
#}

