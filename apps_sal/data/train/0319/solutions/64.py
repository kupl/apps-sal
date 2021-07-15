class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        
        def dfs(start):
            if start >= len(stoneValue):
                return 0
            
            if start in memo:
                return memo[start]
            
            memo[start] = float('-inf') 
            score = 0
            
            for i in range(start, min(len(stoneValue), start + 3)):
                score += stoneValue[i]
                memo[start] = max(memo[start], score - dfs(i + 1))
            
            return memo[start]
        
        score = dfs(0)  
        return 'Tie' if score == 0 else 'Alice' if score > 0 else 'Bob'
