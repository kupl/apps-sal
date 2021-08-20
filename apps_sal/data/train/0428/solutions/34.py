class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:

        def contains(k, v):
            return k // v % 2 == 1
        adjs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        keys = ['a', 'b', 'c', 'd', 'e', 'f']
        locks = [c.upper() for c in keys]
        key_to_val = {k: 2 ** i for (i, k) in enumerate(keys)}
        lock_to_val = {k: 2 ** i for (i, k) in enumerate(locks)}
        (N, M) = (len(grid), len(grid[0]))
        visited = [[[-1] * 64 for _ in range(M)] for _ in range(N)]
        queue = deque()
        target = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '@':
                    queue.append([i, j, 0])
                    visited[i][j][0] = 0
                if grid[i][j] in keys:
                    target += key_to_val[grid[i][j]]
        if target == 0:
            return 0
        while len(queue) > 0:
            (i, j, k) = queue.popleft()
            for (di, dj) in adjs:
                (ii, jj) = (i + di, j + dj)
                if ii >= 0 and jj >= 0 and (ii < N) and (jj < M):
                    if grid[ii][jj] in ('.', '@') and visited[ii][jj][k] < 0:
                        visited[ii][jj][k] = visited[i][j][k] + 1
                        queue.append((ii, jj, k))
                    elif grid[ii][jj] in keys:
                        if not contains(k, key_to_val[grid[ii][jj]]):
                            kk = k + key_to_val[grid[ii][jj]]
                            if kk == target:
                                return visited[i][j][k] + 1
                        else:
                            kk = k
                        if visited[ii][jj][kk] < 0:
                            visited[ii][jj][kk] = visited[i][j][k] + 1
                            queue.append((ii, jj, kk))
                    elif grid[ii][jj] in locks and contains(k, lock_to_val[grid[ii][jj]]) and (visited[ii][jj][k] < 0):
                        visited[ii][jj][k] = visited[i][j][k] + 1
                        queue.append((ii, jj, k))
        return -1
