class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        if not grid:
            return -1
        keys = [0] * 6
        m, n = len(grid), len(grid[0])
        si, sj = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    si, sj = i, j
                if grid[i][j].islower():
                    keys[ord(grid[i][j]) - ord('a')] = 1
        mykeys = tuple(keys)

        q = [(si, sj, tuple([0] * 6))]
        visited = {(si, sj, tuple([0] * 6))}
        c = 0
        while q:
            nextq = []
            for i, j, keys in q:
                for x, y in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != '
                       if grid[x][y] in '.@':
                            if (x, y, keys) not in visited:
                                nextq.append((x, y, keys))
                                visited.add((x, y, keys))
                        elif grid[x][y].islower():
                            okeys = list(keys)
                            okeys[ord(grid[x][y]) - ord('a')] = 1
                            nkeys = tuple(okeys)
                            if nkeys == mykeys:
                                return c + 1
                            else:
                                if (x, y, nkeys) not in visited:
                                    nextq.append((x, y, nkeys))
                                    visited.add((x, y, nkeys))
                        elif grid[x][y].isupper():
                            if keys[ord(grid[x][y].lower()) - ord('a')] == 1 and (x, y, keys) not in visited:
                                nextq.append((x, y, keys))
                                visited.add((x, y, keys))
            c += 1
            q = nextq
        return -1
