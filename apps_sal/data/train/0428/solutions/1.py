class Solution:
    def shortestPathAllKeys(self, grid) -> int:
        from collections import deque
        import copy
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        num_keys = 0
        start = [-1, -1]
        for i in range(rows):
            for j in range(cols):
                ch = grid[i][j]
                if 0 <= ord(ch) - ord('a') <= 5:
                    num_keys += 1
                if ch == '@':
                    start[0] = i
                    start[1] = j
        curr_level = deque()
        next_level = deque()
        visited = set()
        visited.add((0, start[0], start[1]))
        curr_level.append((0, start[0], start[1]))
        steps = 0
        while len(curr_level) > 0:
            for i in range(len(curr_level)):
                ori_keys, x, y = curr_level.popleft()
                for d in dirs:
                    keys = ori_keys
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                        continue
                    ch = grid[new_x][new_y]
                    if ch == '#':
                        continue
                    ascii_minus_lower = ord(ch) - ord('a')
                    ascii_minus_upper = ord(ch) - ord('A')
                    if 0 <= ascii_minus_lower <= 5:
                        keys |= (1 << ascii_minus_lower)
                        if keys == ((1 << num_keys) - 1):
                            return steps + 1
                    if 0 <= ascii_minus_upper <= 5 and (((keys >> ascii_minus_upper) & 1) == 0):
                        continue
                    if (keys, new_x, new_y) not in visited:
                        visited.add((keys, new_x, new_y))
                        next_level.append((keys, new_x, new_y))
            curr_level = copy.deepcopy(next_level)
            next_level.clear()
            steps += 1
        return -1
