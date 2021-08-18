class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        numKeys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j, 0)
                elif ord('a') <= ord(grid[i][j]) <= ord('f'):
                    numKeys += 1
        bfs = [start]
        seen = set()
        d = [1, 0, -1, 0, 1]
        step = 0
        while bfs:
            cur, bfs = bfs, []
            for x, y, keys in cur:
                if keys == (1 << numKeys) - 1:
                    return step
                for i in range(4):
                    xx, yy = x + d[i], y + d[i + 1]
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy, keys) not in seen:
                        seen.add((xx, yy, keys))
                        if ord('a') <= ord(grid[xx][yy]) <= ord('f'):
                            bfs.append((xx, yy, keys | (1 << (ord(grid[xx][yy]) - ord('a')))))
                        elif ord('A') <= ord(grid[xx][yy]) <= ord('F'):
                            if (1 << (ord(grid[xx][yy].lower()) - ord('a'))) & keys == 0:
                                continue
                            else:
                                bfs.append((xx, yy, keys))
                        elif grid[xx][yy] == '.' or grid[xx][yy] == '@':
                            bfs.append((xx, yy, keys))
            step += 1

        return -1
