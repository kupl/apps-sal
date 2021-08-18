class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        keys = 'abcdef'
        locks = 'ABCDEF'
        n, m = len(grid), len(grid[0])
        x, y = -1, -1
        target = 0
        for i in range(n):
            for j in range(m):
                ch = grid[i][j]
                if ch == '@':
                    x, y = i, j
                elif ch in keys:
                    idx = keys.find(ch)
                    target |= (1 << idx)

        visited = set()
        visited.add((x, y, 0))
        q = deque()
        q.append((x, y, 0, 0))
        while q:
            x, y, state, move = q.popleft()
            if state == target:
                return move
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dx += x
                dy += y
                tmp = state
                if dx < 0 or dy < 0 or dx >= n or dy >= m:
                    continue
                ch = grid[dx][dy]
                if ch == '
                continue

                if ch in locks:
                    idx = locks.find(ch)
                    if state & (1 << idx) == 0:
                        continue
                if ch in keys:
                    idx = keys.find(ch)
                    tmp |= (1 << idx)
                if (dx, dy, tmp) not in visited:
                    visited.add((dx, dy, tmp))
                    q.append((dx, dy, tmp, move + 1))
        return -1
