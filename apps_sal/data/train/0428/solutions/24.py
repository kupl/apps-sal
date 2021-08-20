class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        q = collections.deque()
        seen = set()
        tot_keys = 0
        for (i, row) in enumerate(grid):
            for (j, val) in enumerate(row):
                if val == '@':
                    q.append((i, j, 0))
                    seen.add((i, j, 0))
                elif val in 'ABCDEF':
                    tot_keys += 1
        steps = 0
        while q:
            N = len(q)
            for _ in range(N):
                (x, y, keys) = q.popleft()
                if keys == (1 << tot_keys) - 1:
                    return steps
                for (nx, ny) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == '#':
                            continue
                        if grid[nx][ny] in 'ABCDEF' and (not keys >> ord(grid[nx][ny]) - ord('A') & 1):
                            continue
                        nxt = keys
                        if grid[nx][ny] in 'abcdef':
                            nxt |= 1 << ord(grid[nx][ny]) - ord('a')
                        if (nx, ny, nxt) not in seen:
                            seen.add((nx, ny, nxt))
                            q.append((nx, ny, nxt))
            steps += 1
        return -1
