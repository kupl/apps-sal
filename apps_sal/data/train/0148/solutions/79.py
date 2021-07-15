class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        #get best profit by difficulty and apply to each worker
        #init memo table
        m = max(difficulty)
        dp = [0] * m
        for d, p in zip(difficulty, profit):
            dp[d - 1] = max(dp[d - 1], p) 
        for i in range(1,len(dp)):
            dp[i] = max(dp[i], dp[i - 1])    
        return sum([dp[min(w - 1, m - 1)] for w in worker])    

