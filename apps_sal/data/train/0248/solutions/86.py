class Solution:

    def search_cycle(self, grid, i, j, parents):
        key = grid[i][j]
        parents[i, j] = (None, None)
        nodes = [(i, j)]
        visited = set()
        while len(nodes):
            (i, j) = nodes.pop()
            visited.add((i, j))
            (pi, pj) = parents[i, j]
            for (ci, cj) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                in_range = 0 <= ci < len(grid) and 0 <= cj < len(grid[ci])
                is_same_key = in_range and grid[ci][cj] == key
                if ci == pi and cj == pj:
                    continue
                if in_range and is_same_key:
                    if (ci, cj) in visited:
                        return True
                    parents[ci, cj] = (i, j)
                    nodes.append((ci, cj))
        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        parents = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in parents:
                    continue
                is_cycle = self.search_cycle(grid, i, j, parents)
                if is_cycle:
                    return True
        return False
