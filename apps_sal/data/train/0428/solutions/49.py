import heapq
from collections import deque, defaultdict


class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        key_lock_loc = {ch: (i, j) for (i, row) in enumerate(grid) for (j, ch) in enumerate(row) if ch not in {'.', '#'}}
        key_cnt = sum((key_lock.islower() for key_lock in key_lock_loc))

        def bfs_from(src):
            (i, j) = key_lock_loc[src]
            seen = [[False] * n for _ in range(m)]
            seen[i][j] = True
            dque = deque([(i, j, 0)])
            dist = {}
            while dque:
                (i, j, d) = dque.popleft()
                ch = grid[i][j]
                if ch != src and ch != '.':
                    dist[ch] = d
                    continue
                for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if not (0 <= x < m and 0 <= y < n) or grid[x][y] == '#' or seen[x][y]:
                        continue
                    seen[x][y] = True
                    dque.append((x, y, d + 1))
            return dist
        dists = {key_lock: bfs_from(key_lock) for key_lock in key_lock_loc}
        target_state = 2 ** key_cnt - 1
        hq = [(0, '@', 0)]
        final_dist = defaultdict(lambda: float('inf'))
        final_dist['@', 0] = 0
        while hq:
            (d, loc, state) = heapq.heappop(hq)
            if final_dist[loc, state] < d:
                continue
            if state == target_state:
                return d
            for (destination, d2) in list(dists[loc].items()):
                state2 = state
                if destination.islower():
                    state2 |= 1 << ord(destination) - ord('a')
                elif destination.isupper():
                    if not state & 1 << ord(destination) - ord('A'):
                        continue
                if d + d2 < final_dist[destination, state2]:
                    final_dist[destination, state2] = d + d2
                    heapq.heappush(hq, (d + d2, destination, state2))
        return -1
