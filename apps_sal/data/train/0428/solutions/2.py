class Solution:
    def __init__(self):
        self.DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start_x, start_y = -1, -1
        target_keys = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start_x, start_y = i, j
                # elif grid[i][j].islower():
                elif grid[i][j] in 'abcdef':
                    target_keys |= 1 << (ord(grid[i][j]) - ord('a'))
                    # final_keys <<= 1
                    # final_keys |= 1

        pq = [(0, 0, start_x, start_y)]
        visited = set((0, start_x, start_y))

        while pq:
            curr_steps, curr_keys, x, y = heapq.heappop(pq)

            if curr_keys == target_keys:
                return curr_steps

            for delta_x, delta_y in self.DIR:
                next_x, next_y = x + delta_x, y + delta_y

                if not self.inbound(grid, next_x, next_y) or grid[next_x][next_y] == '#':
                    continue

                if grid[next_x][next_y] in 'ABCDEF':
                    if (curr_keys >> (ord(grid[next_x][next_y]) - ord('A'))) & 1:
                        next_keys = curr_keys
                    else:
                        continue
                elif grid[next_x][next_y] in 'abcdef':
                    next_keys = curr_keys | (1 << (ord(grid[next_x][next_y]) - ord('a')))
                else:  # the next location is @ or .
                    next_keys = curr_keys

                if (next_keys, next_x, next_y) in visited:
                    continue

                heapq.heappush(pq, (curr_steps + 1, next_keys, next_x, next_y))
                visited.add((next_keys, next_x, next_y))
        return -1

    def inbound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
