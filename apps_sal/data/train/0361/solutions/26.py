class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        memo = {}
        
        return self.dfs(n, m, memo)
    
    
    
    def dfs(self, x, y, memo):
        if x == 0 or y == 0:
            return 0
        if x == y:
            return 1
        if x == 1:
            return y
        if y == 1:
            return x
        
        if (x, y) in memo:
            return memo[(x, y)]
        
            
        ans = float('inf')
        
        for i in range(1, x):
            ans = min(ans, self.dfs(i, y, memo) + self.dfs(x-i, y, memo))
            
        for j in range(1, y):
            ans = min(ans, self.dfs(x, j, memo) + self.dfs(x, y-j, memo))
        
        
        for side in range(1, min(x, y)):
            for i in range(x-side):
                for j in range(y-side):
                    ans1 = self.dfs(i, j+side, memo)
                    ans2 = self.dfs(x-i, j, memo)
                    ans3 = self.dfs(x-i-side, y-j, memo)
                    ans4 = self.dfs(i+side, y-j-side, memo)
                    
                    ans = min(ans, ans1 + ans2 + ans3 + ans4 + 1)
                    
        memo[(x, y)] = ans
        
        return memo[(x, y)]

