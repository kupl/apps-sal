class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        R = len(grid)
        C = len(grid[0])
        N = R * C
        parents = [i for i in range(N)]
        
        def ufind(a):
            if parents[a] == a:
                return a
            parents[a] = ufind(parents[a])
            return parents[a]
        
        def uunion(a, b):
            aa = ufind(a)
            bb = ufind(b)
            if aa == bb:
                return False
            parents[bb] = aa
            return True
        
        def decode(row, col):
            return row * C + col
        
        for row in range(R):
            for col in range(C):
                if row + 1 < R and grid[row + 1][col] == grid[row][col]:
                    if not uunion(decode(row, col), decode(row + 1, col)):
                        return True
                if col + 1 < C and grid[row][col + 1] == grid[row][col]:
                    if not uunion(decode(row, col), decode(row, col + 1)):
                        return True
                    
        return False
