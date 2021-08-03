class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        sr, sc = 0, 0
        k, m, n = 0, len(grid), len(grid[0])
        key_id = collections.defaultdict(int)
        for i, x in enumerate('abcdef'):
            key_id[x] = i + 1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '@':
                    sr, sc = r, c
                k = max(k, key_id[grid[r][c]])
        q = [(sr, sc, '')]
        res = 0
        vis = set((sr, sc, ''))
        while q:
            tmp = []
            for r, c, keys in q:
                if len(keys) == k:
                    return res
                for rr, cc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] != '#':
                        x = grid[rr][cc]
                        if x in 'ABCDEF' and x.lower() not in keys:
                            continue
                        new_keys = keys[::]
                        if x in 'abcdef' and x not in new_keys:
                            new_keys += x
                        if (rr, cc, new_keys) not in vis:
                            vis.add((rr, cc, new_keys))
                            tmp.append((rr, cc, new_keys))
            res += 1
            q = tmp
        return -1
