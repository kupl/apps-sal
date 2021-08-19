class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:

        def bfs(r, c):
            start = grid[r][c]
            dist[start] = {}
            queue = collections.deque([(r, c, 0)])
            visited = {(r, c): True}
            while queue:
                (i, j, d) = queue.pop()
                if grid[i][j] not in ['.', '#', start]:
                    dist[start][grid[i][j]] = d
                    continue
                for (ic, jc) in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if 0 <= ic < m and 0 <= jc < n and ((ic, jc) not in visited) and (grid[ic][jc] != '#'):
                        visited[ic, jc] = True
                        queue.appendleft((ic, jc, d + 1))
        (m, n) = (len(grid), len(grid[0]))
        dist = {}
        for r in range(m):
            for c in range(n):
                if grid[r][c] not in ['.', '#']:
                    bfs(r, c)
        prioq = [(0, '@', 0)]
        target_state = 0
        visited = {}
        for key in dist:
            if 'a' <= key <= 'f':
                target_state += 1 << ord(key) - ord('a')
        while prioq:
            (d, p, state) = heapq.heappop(prioq)
            if (p, state) in visited:
                continue
            if state == target_state:
                return d
            visited[p, state] = True
            for (dest, moves) in list(dist[p].items()):
                if 'A' <= dest <= 'F' and 1 << ord(dest) - ord('A') & state == 0:
                    continue
                new_state = state
                if 'a' <= dest <= 'f':
                    new_state |= 1 << ord(dest) - ord('a')
                if (dest, new_state) not in visited:
                    heapq.heappush(prioq, (d + moves, dest, new_state))
        return -1
