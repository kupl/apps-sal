class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def find(coords):
            if coords != parents[coords]:
                parents[coords] = find(parents[coords])
            return parents[coords]
        
        def union(point_one, point_two):
            parx, pary = find(point_one), find(point_two)
            if parx != pary:
                if rank[parx] > rank[pary]:
                    parents[pary] = parx
                else:
                    parents[parx] = pary
                    if rank[parx] == rank[pary]:
                        rank[parx] += 1
                # elif rank[parx] < rank[pary]:
                #     parents[parx] = pary
                # else:
                #     parents[parx] = pary
                #     rank[pary] += 1

        if not grid or not grid[0]:
            return False
        m, n = len(grid), len(grid[0])
        
        parents = {(i, j): (i, j) for i in range(m) for j in range(n)}
        rank = collections.Counter()
        
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0 and grid[i-1][j] == grid[i][j-1] == grid[i][j] and find((i-1, j)) == find((i, j-1)):
                    return True
                for r, c in (i-1, j), (i, j-1):
                    if r >= 0 and c >= 0 and grid[r][c] == grid[i][j]:
                        union((r, c), (i, j))
                        
        return False
