class Solution:
    # def minDifficulty(self, A: List[int], d: int) -> int:
    #     if len(A) < d:
    #         return -1
    #     dp = {}
    #     def diff(i,d,maxVal):
    #         if i == len(A):
    #             return 10**9
    #         if d == 1:
    #             return max(maxVal, max(A[i:]))
    #         if (i,d,maxVal) in dp:
    #             return dp[(i,d,maxVal)]
    #         maxVal = max(maxVal,A[i])
    #         dp[(i,d,maxVal)] =  min(diff(i+1,d, maxVal), maxVal+diff(i+1,d-1,0))
    #         return dp[(i,d,maxVal)]
    #     return diff(0,d,0)
    
    def minDifficulty(self, A: List[int], d: int) -> int:
        if len(A) < d:
            return -1
        dp = {}
        def dfs(i,d):
            if d == 1:
                return max(A[i:])
            if (i,d) in dp:
                return dp[(i,d)]
            minVal = float('inf')
            maxNow = 0
            for j in range(i,len(A)-d+1):
                maxNow = max(maxNow, A[j])
                minVal = min(minVal,dfs(j+1,d-1)+maxNow)
            dp[(i,d)] =  minVal
            return dp[(i,d)]
        return dfs(0,d)
    

