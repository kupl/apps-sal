class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_v = max(max(difficulty), max(worker))
        
        n = len(difficulty)
        best = {}
        for i in range(n):
            d = difficulty[i]
            p = profit[i]
            if d not in best:
                best[d] = p
            else:
                best[d] = max(best[d], p)
        
        dp = [0] * (max_v + 1)
        dp[0] = 0
        for i in range (max_v + 1):
            p = 0
            if i in best:
                p = best[i]
            dp[i] = max(dp[i - 1], p)
        
        s = 0 
        for d in worker:
            s += dp[d]
        return s
