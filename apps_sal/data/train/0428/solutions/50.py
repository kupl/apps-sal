class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        (q, seen, keys) = (deque(), set(), set())
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    q.append((i, j, ''))
                    seen.add((i, j, ''))
                elif 'a' <= grid[i][j] <= 'f':
                    keys.add(grid[i][j])
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                (x, y, k) = q.popleft()
                if len(k) == len(keys):
                    return steps
                for (i, j) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    (nx, ny, nk) = (x + i, y + j, k)
                    if nx < 0 or nx >= m or ny < 0 or (ny >= n) or (grid[nx][ny] == '#'):
                        continue
                    if 'A' <= grid[nx][ny] <= 'F' and grid[nx][ny].lower() not in nk:
                        continue
                    if 'a' <= grid[nx][ny] <= 'f' and grid[nx][ny] not in nk:
                        nk += grid[nx][ny]
                    if (nx, ny, nk) not in seen:
                        q.append((nx, ny, nk))
                        seen.add((nx, ny, nk))
            steps += 1
        return -1
