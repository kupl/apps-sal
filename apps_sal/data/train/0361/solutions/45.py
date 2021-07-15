class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        ans = math.inf
        matrix = [[0] * m for _ in range(n)]
        def dfs(r, c, count):
            nonlocal ans
            if count >= ans:
                return 
            
            if r >= n:
                ans = count
                return
            
            if c >= m:
                dfs(r+1, 0, count)
                return
            
            if matrix[r][c]:
                dfs(r, c + 1, count)
                return
            
            for i in range(min(n - r, m - c), 0, -1):
                if not check(r, c, i):
                    break
                
                cover(r, c, i)
                dfs(r, c + i, count + 1)
                uncover(r, c, i)
        
        def check(r, c, k):
            return all(matrix[i][j] == 0 for i in range(r, r + k) for j in range(c, c + k))
        
        def cover(r, c, k):
            for i in range(r, r + k):
                for j in range(c, c + k):
                    matrix[i][j] = 1
        
        def uncover(r, c, k):
            for i in range(r, r + k):
                for j in range(c, c + k):
                    matrix[i][j] = 0
        
        dfs(0, 0, 0)
        return ans
