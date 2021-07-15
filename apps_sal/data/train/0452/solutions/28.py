class Solution:                              
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[float('inf') for _ in range(d+1)] for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1,n+1):
            for k in range(1,d+1):
                tmp_max = 0
                for j in range(i-1,k-2,-1):
                    tmp_max = max(tmp_max,jobDifficulty[j])
                    dp[i][k] = min(dp[i][k],dp[j][k-1]+tmp_max)
        return dp[-1][-1]
        
        
    def minDifficulty_TLE(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                dp[i][j] = max(jobDifficulty[i:j+1])
        # print(dp)
        res = [float('inf')]
        def search(i,j,val): # i- cut, j - idx
            if i == d:
                res[0] = min(res[0],val+(0 if j >= n else dp[j][-1]))
                return
            for k in range(j,n):
                search(i+1,k+1,val+dp[j][k])
        search(0,0,0)
        return res[0]

