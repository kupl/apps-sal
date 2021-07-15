class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        
        node_par = {}
        for i in range(n):
            for j in range(m):
                node_par[(i, j)] = (i, j)
                
        dxdys = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        def find_par(par):
            path = []
            while node_par[par] != par:
                path.append(par)
                par = node_par[par]
            for tmp in path:
                node_par[tmp] = par
            return par
        
        for x in range(n):
            for y in range(m):
                if (x + y) % 2:
                    continue
                    
                for dx, dy in dxdys:
                    x_new, y_new = x + dx, y + dy
                    if not (0 <= x_new < n and 0 <= y_new < m) or grid[x_new][y_new] != grid[x][y]:
                        continue
                    
                    curr_par = find_par((x, y))
                    new_par = find_par((x_new, y_new))
                    if curr_par == new_par:
                        return True
                    node_par[curr_par] = new_par
                    
        return False

