from collections import defaultdict, deque
import heapq


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        ord_a = ord('a')
        ord_A = ord('A')
        m, n = len(grid), len(grid[0])
        key_lock_loc = {ch: (i, j) for i, row in enumerate(grid) for j, ch in enumerate(row) if ch not in '.
        key_cnt = sum(ch.islower() for ch in key_lock_loc)

        def dfs_from(src):
            i, j = key_lock_loc[src]
            dque = deque([(i, j, 0)])
            seen = defaultdict(lambda: False)
            seen[i, j] = True
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
                    dque.append((x, y, d + 1))
                    seen[x, y] = True
            return dist

        dists = {ch: dfs_from(ch) for ch in key_lock_loc}
        final_dist = defaultdict(lambda: float('inf'))
        hq = [(0, '@', 0)]
        final_state = 2**key_cnt - 1

        while hq:
            d, ch, state = heapq.heappop(hq)
            if d > final_dist[ch, state]:
                continue
            if state == final_state:
                return d
            for ch1, d1 in list(dists[ch].items()):
                state1 = state
                if ch1.islower():
                    state1 |= 1 << (ord(ch1) - ord_a)
                elif ch1.isupper():
                    if not (state1 & 1 << (ord(ch1) - ord_A)):
                        continue
                if d + d1 < final_dist[ch1, state1]:
                    final_dist[ch1, state1] = d + d1
                    heapq.heappush(hq, (d + d1, ch1, state1))
        return -1
