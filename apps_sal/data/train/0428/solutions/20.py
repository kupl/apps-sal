class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = collections.deque()
        keys = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    q.append((i, j, 0))
                    visited.add((i, j, 0))
                elif grid[i][j] >= 'a' and grid[i][j] <= 'f':
                    keys += 1
        goal = (1 << keys) - 1

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j, state = q.popleft()
                for di, dj in dirs:
                    x = i + di
                    y = j + dj

                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '
                    continue

                    nstate = state
                    if grid[x][y] >= 'A' and grid[x][y] <= 'F':
                        temp = ord(grid[x][y]) - ord('A')
                        if state & (1 << temp) == 0:
                            continue
                    elif grid[x][y] >= 'a' and grid[x][y] <= 'f':
                        temp = ord(grid[x][y]) - ord('a')
                        nstate |= 1 << temp
                        if nstate == goal:
                            return step + 1

                    visited.add((x, y, nstate))
                    q.append((x, y, nstate))

            step += 1

        return -1
