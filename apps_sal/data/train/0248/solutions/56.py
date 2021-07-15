from collections import defaultdict
class Solution:
    DELTA = [(0,-1),(0,1),(-1,0),(1,0)]
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfsCycle(grid, R, C, p_r, p_c, r, c, visited, grp, grp_num):
            if (r, c) in grp[grp_num]:
                return True
            
            # check 4 directions
            visited.add((r,c))
            grp[grp_num].add((r,c))
            result = False
            for d in Solution.DELTA:
                n_r = r + d[0]
                n_c = c + d[1]
                if 0 <= n_r < R and 0 <= n_c < C and not (p_r == n_r and p_c == n_c) and grid[n_r][n_c] == grid[r][c]:
                    result |= dfsCycle(grid, R, C, r, c, n_r, n_c, visited, grp, grp_num)
                    if result:
                        break
                    
            return result
            
        R = len(grid)
        C = len(grid[0])
        visited = set()
        grp_num = 0
        grp = defaultdict(set)
        for r in range(R):
            for c in range(C):
                if (r,c) not in visited:
                    grp_num += 1
                    if dfsCycle(grid, R, C, r, c, r, c, visited, grp, grp_num):
                        return True
                    
        return False
