class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        from collections import deque

        queue = deque()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    queue.append((i, j, None, None))

        dist = {}
        while queue:

            i, j, previ, prevj = queue.popleft()
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                continue
            if (i, j) not in dist:
                dist[(i, j)] = 1 + dist.get((previ, prevj), -1)
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    newi, newj = i + di, j + dj
                    queue.append((newi, newj, i, j))

        ans = max(list(dist.values()), default=-1)
        return ans if ans != 0 else -1
