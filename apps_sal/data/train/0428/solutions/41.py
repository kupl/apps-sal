class Solution:

    def __init__(self):
        self.DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        init_x = init_y = -1
        target_keys = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    (init_x, init_y) = (i, j)
                elif grid[i][j].islower():
                    target_keys |= 1 << ord(grid[i][j]) - ord('a')
        pq = [(0, 0, init_x, init_y)]
        visited = set((0, init_x, init_y))
        while pq:
            (curr_steps, curr_keys, x, y) = heapq.heappop(pq)
            if curr_keys == target_keys:
                return curr_steps
            for (delta_x, delta_y) in self.DIR:
                (next_x, next_y) = (x + delta_x, y + delta_y)
                if not self.inbound(grid, next_x, next_y) or grid[next_x][next_y] == '#':
                    continue
                if grid[next_x][next_y].isupper():
                    if curr_keys >> ord(grid[next_x][next_y]) - ord('A') & 1:
                        next_keys = curr_keys
                    else:
                        continue
                elif grid[next_x][next_y].islower():
                    next_keys = curr_keys | 1 << ord(grid[next_x][next_y]) - ord('a')
                else:
                    next_keys = curr_keys
                if (next_keys, next_x, next_y) in visited:
                    continue
                heapq.heappush(pq, (curr_steps + 1, next_keys, next_x, next_y))
                visited.add((next_keys, next_x, next_y))
        return -1

    def inbound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
