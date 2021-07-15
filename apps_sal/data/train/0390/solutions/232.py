class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(stones):
            if stones <= 0:
                return False
            
            for i in reversed(list(range(1, int(sqrt(stones)) + 1))):
                square = i*i
                if stones - square == 0 or not dfs(stones - square):
                    return True
                
            return False
        
        return dfs(n)
    
    

