class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        parents = {}
        def find(p):
            if p not in parents:
                parents[p] = p
            if parents[p] != p:
                parents[p] = find(parents[p])
            return parents[p]
        def is_connected(p, q):
            return find(p) == find(q)
        def union(p, q):
            i, j = find(p), find(q)
            parents[j] = i
            
        R, C = len(grid), len(grid[0])
        
        for r in range(R):
            for c in range(C):
                for nr, nc in [r+1, c], [r, c+1]:
                    if nr < R and nc < C and grid[r][c] == grid[nr][nc]:
                        if is_connected((r, c), (nr, nc)):
                            return True
                        union((r, c), (nr, nc))
        
        return False
