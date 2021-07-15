from collections import deque
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        k = 0
        m, n = len(grid), len(grid[0])
        sr, sc = None, None
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '@':
                    sr, sc = r, c
                elif grid[r][c] in 'abcdefABCDEF':
                    k = max(k, ord(grid[r][c].lower()) - ord('a') + 1)
        dp = [[[float('inf') for z in range(1 << k)] for y in range(n)] for x in range(m)]
        dp[sr][sc][0] = 0
        dq = deque([(sr, sc, 0, 0)])
        while dq:
            size = len(dq)
            for i in range(size):
                r, c, ks, s = dq.popleft() # key state, step
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if not (0 <= nr < m) or not (0 <= nc < n):
                        continue
                    elif grid[nr][nc] == '#':
                        continue
                    elif grid[nr][nc] in '.@': # empty cell or starting point
                        if s + 1 < dp[nr][nc][ks]:
                            dp[nr][nc][ks] = s + 1
                            dq.append((nr, nc, ks, s + 1))
                    elif grid[nr][nc] in 'ABCDEF':
                        lock = ord(grid[nr][nc]) - ord('A')
                        if ks & (1 << lock):
                            if s + 1 < dp[nr][nc][ks]:
                                dp[nr][nc][ks] = s + 1
                                dq.append((nr, nc, ks, s + 1))
                    elif grid[nr][nc] in 'abcdef':
                        key = ord(grid[nr][nc]) - ord('a')
                        nks = ks | (1 << key)
                        if s + 1 < dp[nr][nc][nks]:
                            dp[nr][nc][nks] = s + 1
                            dq.append((nr, nc, nks, s + 1))
        ret = float('inf')
        for r in range(m):
            for c in range(n):
                ret = min(ret, dp[r][c][-1])
        return ret if ret != float('inf') else -1
                

