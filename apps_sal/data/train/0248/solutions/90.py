import collections


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        '''
        # dfs, TLE. I think bfs will leads to TLE as well.
        rows, cols = len(grid), len(grid[0])
        def dfs(ch, s_r, s_c, row, col, seen, leng):
            for dr, dc in [[1, 0],[0, -1], [0, 1], [-1, 0]]:
                r, c = row + dr, col + dc
                if leng >= 4 and (r, c) == (s_r, s_c):
                    return True
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == ch and (r, c) not in seen and dfs(ch, s_r, s_c, r, c, seen | set([(r, c)]), leng + 1):
                    return True
            return False

        for r in range(rows - 1):
            for c in range(cols - 1):
                if grid[r][c] == grid[r + 1][c] == grid[r][c + 1]:
                    if dfs(grid[r][c], r, c, r, c, set([(r, c)]), 1):
                        return True
        return False
        '''
        # Union Find, when you reach a char which is the same as current char and the two share the same
        # ancestor, then there is a ring
        rows, cols = len(grid), len(grid[0])
        seen = set()
        ancestors = dict()
        for r in range(rows):
            for c in range(cols):
                ancestors[(r, c)] = (r, c)

        def find(x, y):
            if ancestors[(x, y)] != (x, y):
                xx, yy = ancestors[(x, y)]
                ancestors[(x, y)] = find(xx, yy)
            return ancestors[(x, y)]

        def union(x1, y1, x2, y2):
            # (x2, y2) is the new char that should be added to the group that (x1, y1) belongs to
            ancestors[find(x2, y2)] = find(x1, y1)

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                if r > 0 and c > 0 and grid[r - 1][c] == grid[r][c - 1] == grid[r][c] and find(r - 1, c) == find(r, c - 1):
                    return True
                if c > 0 and grid[r][c - 1] == grid[r][c]:
                    union(r, c - 1, r, c)
                if r > 0 and grid[r - 1][c] == grid[r][c]:
                    union(r, c, r - 1, c)
        return False


'''
[[\"a\",\"a\",\"a\",\"a\"],[\"a\",\"b\",\"b\",\"a\"],[\"a\",\"b\",\"b\",\"a\"],[\"a\",\"a\",\"a\",\"a\"]]
[[\"c\",\"c\",\"c\",\"a\"],[\"c\",\"d\",\"c\",\"c\"],[\"c\",\"c\",\"e\",\"c\"],[\"f\",\"c\",\"c\",\"c\"]]
[[\"a\",\"b\",\"b\"],[\"b\",\"z\",\"b\"],[\"b\",\"b\",\"a\"]]
[[\"d\",\"b\",\"b\"],[\"c\",\"a\",\"a\"],[\"b\",\"a\",\"c\"],[\"c\",\"c\",\"c\"],[\"d\",\"d\",\"a\"]]
'''
