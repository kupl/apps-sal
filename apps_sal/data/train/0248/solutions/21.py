class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        (h, w) = (len(grid), len(grid[0]))

        def in_range(x, y):
            return 0 <= x < w and 0 <= y < h

        def four_neighbors(x, y):
            for (dx, dy) in {(+1, 0), (-1, 0), (0, +1), (0, -1)}:
                (next_x, next_y) = (x + dx, y + dy)
                if in_range(next_x, next_y):
                    yield (next_x, next_y)

        def dfs(x, y, prev_x, prev_y, grid):
            if grid[y][x] == dfs.cur_symbol:
                return True
            grid[y][x] = dfs.cur_symbol
            for (next_x, next_y) in four_neighbors(x, y):
                if (next_x, next_y) == (prev_x, prev_y):
                    continue
                elif grid[next_y][next_x].upper() != dfs.cur_symbol:
                    continue
                if dfs(next_x, next_y, x, y, grid):
                    return True
            return False
        failed_symbol = set()
        for y in range(h):
            for x in range(w):
                dfs.cur_symbol = grid[y][x]
                if dfs.cur_symbol in failed_symbol:
                    continue
                dfs.cur_symbol = grid[y][x].upper()
                if dfs(x, y, -1, -1, grid):
                    return True
                else:
                    failed_symbol.add(dfs.cur_symbol)
        return False
