class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        init_x, init_y = -1, -1
        m = len(grid)
        n = len(grid[0])
        keycnt = 0

        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    init_x, init_y = i, j
                if c >= 'a' and c <= 'f':
                    keycnt += 1

        init_state = (0, init_x, init_y)
        q = collections.deque()
        visited = set()
        visited.add(init_state)
        q.append(init_state)
        steps = -1
        finalkey = 0

        for i in range(keycnt):
            finalkey |= (1 << i)

        while q:
            lens = len(q)
            steps += 1

            for _ in range(len(q)):
                keys, x, y = q.popleft()
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):

                    if 0 > nx or nx >= m or 0 > ny or ny >= n:
                        continue

                    new_s = keys
                    c = grid[nx][ny]
                    if c == '
                    continue

                    if c >= 'A' and c <= 'F' and ((keys >> (ord(c) - ord('A'))) & 1 == 0):
                        continue

                    if c >= 'a' and c <= 'f':
                        new_s |= (1 << (ord(c) - ord('a')))

                    if (new_s, nx, ny) in visited:
                        continue
                    if new_s == finalkey:
                        return steps + 1

                    visited.add((new_s, nx, ny))
                    q.append((new_s, nx, ny))

        return -1
