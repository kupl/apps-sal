class Solution:
    def containsCycle(self, grid) -> bool:
        if not grid or not grid[0]: return False
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited=[[False] * len(grid[i]) for i in range(len(grid))]
                
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j]:
                    stack = [(i, j, 0, 0)]
                    visited[i][j] = True
                    symbol = grid[i][j]
                    
                    while stack:
                        row, col, prev_row, prev_col = stack.pop()

                        for direction in directions:
                            nr = row + direction[0]
                            nc = col + direction[1]

                            if nr == prev_row and nc == prev_col:
                                continue
                            if len(grid) > nr >= 0 and len(grid[nr]) > nc >= 0 and grid[nr][nc] == symbol:
                                if visited[nr][nc]:
                                    return True
                                else:
                                    visited[nr][nc] = True
                                    stack.append((nr, nc, row, col))
                      
        return False
