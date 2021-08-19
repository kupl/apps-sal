class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        k = 0
        (stx, sty) = (0, 0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] in 'abcdef':
                    k += 1
                if grid[i][j] == '@':
                    stx = i
                    sty = j

        def keys(mask):
            ans = 0
            for m in [1, 2, 4, 8, 16, 32]:
                if mask & m:
                    ans += 1
            return ans

        def neighbors(i, j):
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if i + dx < 0 or i + dx >= m or j + dy < 0 or (j + dy >= n):
                    continue
                if grid[i + dx][j + dy] == '#':
                    continue
                yield (i + dx, j + dy)
        q = collections.deque()
        seen = set()
        q.append((stx, sty, 0, 0))
        while q:
            (i, j, mask, moves) = q.popleft()
            if grid[i][j] in 'ABCDEF':
                id = 'ABCDEF'.index(grid[i][j])
                if not mask & 1 << id:
                    continue
            if (i, j, mask) in seen:
                continue
            seen.add((i, j, mask))
            if keys(mask) == k:
                return moves - 1
            if grid[i][j] in 'abcdef':
                mask |= 1 << ord(grid[i][j]) - ord('a')
            for (ii, jj) in neighbors(i, j):
                q.append((ii, jj, mask, moves + 1))
        return -1
