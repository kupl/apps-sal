class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d*f < target: return 0
        if d*f == target: return 1
        
        def dfs(j,left,memo):
            
            if (j,left) in memo.keys():
                return memo[(j,left)]
            
            if left < 0:
                return 0
            
            if j == d-1:
                return int(left > 0 and left <= f)
            
            ans = 0
            for i in range(1,f+1):
                ans += dfs(j+1,left-i,memo)
            
            memo[(j,left)] = ans
            
            return memo[(j,left)]
        
        return dfs(0,target,{}) % (10 ** 9 + 7)
