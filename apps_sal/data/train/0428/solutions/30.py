class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        if not grid or not grid[0]:
            return -1
        (m, n) = (len(grid), len(grid[0]))
        sx = sy = target = -1
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    (sx, sy) = (i, j)
                if c >= 'a' and c <= 'f':
                    target = max(target, ord(c) - ord('a') + 1)
        target = (1 << target) - 1
        q = deque([(sx, sy, 0)])
        visited = set()
        visited.add(q[0])
        step = 0
        while q:
            for _ in range(len(q)):
                (x, y, key) = q.popleft()
                if key == target:
                    return step
                for (i, j) in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    if x + i >= 0 and x + i < m and (y + j >= 0) and (y + j < n):
                        c = grid[x + i][y + j]
                        new_key = key
                        if c == '#':
                            continue
                        if c >= 'A' and c <= 'F' and (key >> ord(c) - ord('A') & 1 == 0):
                            continue
                        if c >= 'a' and c <= 'f':
                            new_key |= 1 << ord(c) - ord('a')
                        if (x + i, y + j, new_key) not in visited:
                            visited.add((x + i, y + j, new_key))
                            q.append((x + i, y + j, new_key))
            step += 1
        return -1
