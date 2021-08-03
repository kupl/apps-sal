class Solution:
    def expandIsland(self, grid, i, j):
        edges = [(i, j)]
        while edges:
            next_edges = []
            for edge in edges:
                ei, ej = edge
                if ei >= 0 and ei < len(grid) and ej >= 0 and ej < len(grid[ei]) and grid[ei][ej] == '1':
                    grid[ei][ej] = '2'
                    next_edges.append((ei + 1, ej))
                    next_edges.append((ei, ej + 1))
                    next_edges.append((ei - 1, ej))
                    next_edges.append((ei, ej - 1))
            edges = next_edges

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    island_count += 1
                    self.expandIsland(grid, i, j)
        return island_count
