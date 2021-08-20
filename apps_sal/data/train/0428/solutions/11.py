class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        (row, col) = (len(grid), len(grid[0]))
        (x, y) = (None, None)
        num_keys = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '@':
                    (x, y) = (r, c)
                elif grid[r][c] in 'abcdef':
                    num_keys += 1
        queue = collections.deque([(x, y, 0, 0, '.@abcdef')])
        dires = [1, 0, -1, 0, 1]
        visited = set()
        while queue:
            (r, c, steps, cnt_keys, accessible) = queue.popleft()
            if grid[r][c] in 'abcdef' and grid[r][c].upper() not in accessible:
                accessible += grid[r][c].upper()
                cnt_keys += 1
            if cnt_keys == num_keys:
                return steps
            for d in range(len(dires) - 1):
                (new_r, new_c) = (r + dires[d], c + dires[d + 1])
                if 0 <= new_r < row and 0 <= new_c < col and (grid[r][c] in accessible):
                    if (new_r, new_c, accessible) not in visited:
                        visited.add((new_r, new_c, accessible))
                        queue.append((new_r, new_c, steps + 1, cnt_keys, accessible))
        return -1
