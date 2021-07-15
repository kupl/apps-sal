from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        right, left, down, up = (0, 1), (0, -1), (1, 0), (-1, 0)
        
        direction_map = {
            1: right,
            2: left,
            3: down,
            4: up
        }
        
        directions = [right, left, down, up]
        visited = set()
        
        def in_bounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[i])
        
        def dfs(i, j):                                           
            # not in bounds
            if not in_bounds(i, j) or (i, j) in visited:
                return []
            
            visited.add((i, j))

            sign = grid[i][j]
            direction = direction_map[sign]
            next_i, next_j = i + direction[0], j + direction[1]
            return [(i, j)] + dfs(next_i, next_j)
                
                    
        reachable = dfs(0, 0)
        curr_cost = 0
        while reachable:
            next_reachable = []
            for (i, j) in reachable:
                if i == len(grid) - 1 and j == len(grid[i]) - 1:
                    return curr_cost
                
                for d in directions:
                    next_reachable += dfs(i + d[0], j + d[1])
            reachable = next_reachable
            curr_cost += 1
                    
        return -1
                
                    

