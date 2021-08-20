class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:

        def have_keys(status, key_id):
            return status & 2 ** key_id
        (sx, sy) = (-1, -1)
        key_number = 0
        key_idx = 'abcdef'
        lock_idx = 'ABCDEF'
        (n, m) = (len(grid), len(grid[0]))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    (sx, sy) = (i, j)
                elif grid[i][j] in key_idx:
                    key_number = max(key_number, key_idx.find(grid[i][j]))
        final_ownkey = 2 ** (key_number + 1) - 1
        (head, queue) = (0, [(sx, sy, 0)])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {(sx, sy, 0): 0}
        while head < len(queue):
            (x, y, status) = queue[head]
            step = visited[queue[head]]
            for (dx, dy) in moves:
                (tx, ty, new_status) = (x + dx, y + dy, status)
                if n > tx >= 0 and m > ty >= 0:
                    if grid[tx][ty] == '#':
                        continue
                    if grid[tx][ty] in lock_idx and (not have_keys(new_status, lock_idx.find(grid[tx][ty]))):
                        continue
                    if grid[tx][ty] in key_idx and (not have_keys(new_status, key_idx.find(grid[tx][ty]))):
                        new_status += 2 ** key_idx.find(grid[tx][ty])
                    if new_status == final_ownkey:
                        return step + 1
                    if (tx, ty, new_status) not in visited:
                        queue.append((tx, ty, new_status))
                        visited[tx, ty, new_status] = step + 1
            head += 1
        return -1
