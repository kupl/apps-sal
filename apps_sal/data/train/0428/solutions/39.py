class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        R, C = len(grid), len(grid[0])
        ii, jj = 0, 0
        target = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '@':
                    ii, jj = i, j
                if grid[i][j].islower():
                    target += 1

        def bfs(i, j):
            from collections import deque
            Q = deque([(i, j, 0, set())])
            seen = {(i, j, tuple(sorted(set())))}
            while Q:
                i, j, d, s = Q.popleft()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r, c = i + di, j + dj
                    if 0 <= r < R and 0 <= c < C:
                        if grid[r][c].islower():
                            #s1 = s
                            s1 = s.copy()
                            s1.add(grid[r][c])
                            if len(s1) == target:
                                return d + 1
                            tuple_s = tuple(sorted(set(s1)))
                            if (r, c, tuple_s) not in seen:
                                seen.add((r, c, tuple_s))
                                Q.append((r, c, d + 1, s1))
                        elif grid[r][c].isupper():
                            if grid[r][c].lower() in s:
                                tuple_s = tuple(sorted(set(s)))
                                if (r, c, tuple_s) not in seen:
                                    seen.add((r, c, tuple_s))
                                    Q.append((r, c, d + 1, s))
                        elif grid[r][c] != '#':
                            tuple_s = tuple(sorted(set(s)))
                            if (r, c, tuple_s) not in seen:
                                seen.add((r, c, tuple_s))
                                Q.append((r, c, d + 1, s))
            return -1
        return bfs(ii, jj)
