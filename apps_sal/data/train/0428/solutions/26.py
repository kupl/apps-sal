from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        n = len(grid[0])
        visited = set()
        q = deque()
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    q.append((i, j, 0))
                    visited.add((i, j, 0))
                elif grid[i][j] in 'abcdef':
                    cnt += 1

        keys = set('abcdef')
        locks = set('ABCDEF')
        target = 2**(cnt) - 1
        steps = 0
        while len(q) > 0:
            # for _ in range(3):
            q_sz = len(q)
            for _ in range(q_sz):
                x, y, cur_keys = q.popleft()
                # print(\"steps\", steps, \":\", x, y, cur_keys)
                if cur_keys == target:
                    return steps
                for d in dirs:
                    next_x, next_y = x + d[0], y + d[1]
                    pos_flag = False
                    if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] != '#':
                        new_keys = cur_keys
                        if grid[next_x][next_y] in locks:
                            lock = ord(grid[next_x][next_y]) - ord('A')
                            if (1 << lock) & cur_keys != 0:
                                pos_flag = True
                        elif grid[next_x][next_y] in keys:
                            key = ord(grid[next_x][next_y]) - ord('a')
                            new_keys = cur_keys | (1 << key)
                            pos_flag = True
                        else:
                            pos_flag = True

                        if pos_flag and (next_x, next_y, new_keys) not in visited:
                            # print(\"steps\", steps, \":\", next_x, next_y, cur_keys)
                            visited.add((next_x, next_y, new_keys))
                            q.append((next_x, next_y, new_keys))
            steps += 1
        return -1
# [\"@.a.#\",\"###.#\",\"b.A.B\"]
# [\"@..aA\",\"..B#.\",\"....b\"]
