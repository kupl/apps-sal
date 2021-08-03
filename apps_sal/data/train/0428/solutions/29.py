class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        mx_key = max(grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j].isalpha() and grid[i][j].islower())
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    si, sj = i, j
                    break
        needed_keys = (1 << (ord(mx_key) - ord('a') + 1)) - 1

        def key_id(c):
            if c.isupper():
                return ord(c) - ord('A'), True
            return ord(c) - ord('a'), False  # id, upper
        seen = {(si, sj, 0)}
        q = deque([(0, si, sj, 0)])  # cost,i,j,keys
        while q:
            cost, i, j, keys = q.popleft()
            if keys == needed_keys:
                return cost
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not 0 <= ni < len(grid) or not 0 <= nj < len(grid[0]) or grid[ni][nj] == '#':
                    continue
                # get new keys bitset
                new_keys = keys
                if grid[ni][nj].isalpha():
                    idx, capped = key_id(grid[ni][nj])
                    if capped:
                        if not keys & (1 << idx):
                            continue  # cant enter a door we dont have a key to
                    else:
                        new_keys |= 1 << idx
                if (ni, nj, new_keys) in seen:
                    continue
                seen.add((ni, nj, new_keys))
                q.append((cost + 1, ni, nj, new_keys))
        return -1
