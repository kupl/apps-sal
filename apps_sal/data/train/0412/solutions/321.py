class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        
        @lru_cache(None)
        def dfs(left, k):
            if left == k:
                return 1
            
            if left > k:
                return 0
            
            if k == 0:
                if left == 0:
                    return 1
                else:
                    return 0
            
            if left < 0 :
                return 0
            
            
            s = 0
            for i in range(1, f+1):
                if k - i < 0:
                    break
                s += dfs(left-1, k - i)
            
            return s % (10 ** 9 + 7)
        
        return dfs(d, target) % (10 ** 9 + 7)
