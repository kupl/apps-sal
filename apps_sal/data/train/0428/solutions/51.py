class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        target = 0
        queue, visited = [], set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if 'a' <= grid[i][j] <= 'f':
                    target += 1
                elif grid[i][j] == '@':
                    queue.append((i, j, '.@abcdef', 0))
                    visited.add((i, j, '.@abcedf'))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        collected = set()

        while len(queue) != 0:
            size = len(queue)
            for _ in range(size):
                x, y, bag, collected = queue.pop(0)
                if collected == target:
                    return ans
                for ix, iy in dirs:
                    xx = x + ix
                    yy = y + iy
                    if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]) and grid[xx][yy] in bag:
                        if 'a' <= grid[xx][yy] <= 'f' and grid[xx][yy].upper() not in bag:
                            if (xx, yy, bag + grid[xx][yy].upper()) not in visited:
                                queue.append((xx, yy, bag + grid[xx][yy].upper(), collected + 1))
                                visited.add((xx, yy, bag + grid[xx][yy].upper()))
                        else:
                            if (xx, yy, bag) not in visited:
                                queue.append((xx, yy, bag, collected))
                                visited.add((xx, yy, bag))
            ans += 1
        return -1
