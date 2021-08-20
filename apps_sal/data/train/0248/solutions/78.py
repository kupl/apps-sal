class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        (m, n) = (len(grid), len(grid[0]))
        ve = collections.defaultdict(set)
        for (i, row) in enumerate(grid):
            for (j, val) in enumerate(row):
                ve[val].add((i, j))
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def check(k):
            visiting = set()
            visited = set()
            v = ve[k]

            def dfs(curr, prev):
                if curr in visiting:
                    return True
                visiting.add(curr)
                (x, y) = curr
                for (dx, dy) in dxy:
                    (x2, y2) = (x + dx, y + dy)
                    if 0 <= x2 < m and 0 <= y2 < n and ((x2, y2) != prev) and ((x2, y2) in v):
                        if dfs((x2, y2), curr):
                            return True
                visiting.remove(curr)
                visited.add(curr)
                return False
            for a in v:
                if a not in visited:
                    if dfs(a, None):
                        return True
            return False
        for k in ve:
            if check(k):
                return True
        return False
