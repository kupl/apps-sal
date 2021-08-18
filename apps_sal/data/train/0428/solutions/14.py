import heapq
from collections import deque, defaultdict


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        key_lock_loc = {ch: (i, j) for i, row in enumerate(grid) for j, ch in enumerate(row) if ch not in {'.', '
        key_cnt = sum(key_lock.islower() for key_lock in key_lock_loc)

        def bfs_from(src):
            i, j = key_lock_loc[src]
            seen = [[False] * n for _ in range(m)]
            seen[i][j] = True
            dque = deque([(i, j, 0)])
            dist = {}
            while dque:
                i, j, d = dque.popleft()
                ch = grid[i][j]
                if ch != src and ch != '.':
                    dist[ch] = d
                    continue
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if not (0 <= x < m and 0 <= y < n) or grid[x][y] == '
                        continue
                    seen[x][y] = True
                    dque.append((x, y, d + 1))
            return dist

        dists = {key_lock: bfs_from(key_lock) for key_lock in key_lock_loc}
        all_keys_bitmap = 2 ** key_cnt - 1

        hq = [(0, '@', 0)]
        final_dist = defaultdict(lambda: float('inf'))
        final_dist['@', 0] = 0
        while hq:
            d, ch, keys_bitmap = heapq.heappop(hq)
            if final_dist[ch, keys_bitmap] < d:
                continue
            if keys_bitmap == all_keys_bitmap:
                return d
            for next_key_lock, d2 in list(dists[ch].items()):
                keys_bitmap2 = keys_bitmap
                if next_key_lock.islower():
                    keys_bitmap2 |= (1 << (ord(next_key_lock) - ord('a')))
                elif next_key_lock.isupper():
                    if not(keys_bitmap & (1 << (ord(next_key_lock) - ord('A')))):
                        continue
                if d + d2 < final_dist[next_key_lock, keys_bitmap2]:
                    final_dist[next_key_lock, keys_bitmap2] = d + d2
                    heapq.heappush(hq, (d + d2, next_key_lock, keys_bitmap2))
        return -1
