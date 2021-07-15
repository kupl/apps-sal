class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if N < d:
            return -1

        dp = [[-1] * (d + 1) for _ in range(N)]
        
        def dfs(idx, d):
            if d == 0:
                if idx == N:
                    return 0
                else:
                    return math.inf
            
            if idx == N:
                return math.inf
            
            if dp[idx][d] != -1:
                return dp[idx][d]
            
            res = math.inf
            day_max = 0
            
            for j in range(idx, N):
                day_max = max(day_max, jobDifficulty[j])
                res = min(res, day_max + dfs(j + 1, d - 1))


            dp[idx][d] = res
            return res
        
        return dfs(0, d)
