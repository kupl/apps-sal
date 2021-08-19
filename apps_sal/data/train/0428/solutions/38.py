class Solution:

    def shortestPathAllKeys(self, grid) -> int:
        (row, col) = (len(grid), len(grid[0]))
        (key_num, key) = (0, {})
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '@':
                    (start_i, start_j) = (i, j)
                if grid[i][j] in 'abcdef' and grid[i][j] not in key:
                    key[grid[i][j]] = key_num
                    key_num += 1
        q = [(start_i, start_j, 0, 0)]
        visited = set()
        while q:
            l = len(q)
            for _ in range(l):
                (i, j, state, step) = q.pop(0)
                if state == (1 << key_num) - 1:
                    return step
                if (i, j, state) in visited:
                    continue
                visited.add((i, j, state))
                for (m, n) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= m < row and 0 <= n < col and (grid[m][n] != '#'):
                        if grid[m][n] in 'abcdef':
                            q.append((m, n, state | 1 << key[grid[m][n]], step + 1))
                        elif grid[m][n] == '.' or grid[m][n] == '@':
                            q.append((m, n, state, step + 1))
                        elif grid[m][n] in 'ABCDEF':
                            if state >> key[grid[m][n].lower()] & 1 == 0:
                                continue
                            q.append((m, n, state, step + 1))
        return -1
