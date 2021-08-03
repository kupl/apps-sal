class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        n, m = len(grid), len(grid[0])

        startx, starty = -1, -1
        nkeys = 0

        for i in range(n):

            for j in range(m):

                if grid[i][j] == '@':

                    startx, starty = i, j

                if grid[i][j] in 'abcdef':

                    nkeys += 1

        queue = deque([(startx, starty, 0, '', 0)])

        visited = set([(startx, starty, '')])

        while queue:

            node = queue.popleft()

            x, y, nkey, keys, moves = node

            if nkey == nkeys:
                return moves

            for ni in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:

                xx, yy = ni

                if xx < 0 or yy < 0 or xx >= n or yy >= m or grid[xx][yy] == '#':
                    continue

                if grid[xx][yy] in 'ABCDEF':
                    if grid[xx][yy].lower() in keys and (xx, yy, keys) not in visited:
                        queue.append(((xx, yy, nkey, keys, moves + 1)))
                        visited.add((xx, yy, keys))

                elif grid[xx][yy] in 'abcdef' and grid[xx][yy] not in keys:
                    visited.add((xx, yy, keys + grid[xx][yy]))
                    queue.append((xx, yy, nkey + 1, keys + grid[xx][yy], moves + 1))

                elif (xx, yy, keys) not in visited:
                    visited.add((xx, yy, keys))
                    queue.append((xx, yy, nkey, keys, moves + 1))

        return -1
