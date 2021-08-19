'''
[\"@.a.#\",\"###.#\",\"b.A.B\"]

[
\"@.a.#\",
\"###.#\",
\"b.A.B\"
]


[
\"@..aA\",
\"..B#.\",
\"....b\"
]


'''


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])

        queue = collections.deque()
        seen = set()
        nKeys = 0
        moves = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    queue.append([i, j, 0, 0, 'abcdef.@'])
                elif grid[i][j] in 'abcdef':
                    nKeys += 1

        while queue:
            i, j, moves, curKeys, keys = queue.popleft()

            if grid[i][j] in 'abcdef' and grid[i][j].upper() not in keys:
                keys += grid[i][j].upper()
                curKeys += 1

            if curKeys == nKeys:
                return moves

            for x, y in (-1, 0), (1, 0), (0, -1), (0, 1):
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] in keys and (ni, nj, keys) not in seen:
                    seen.add((ni, nj, keys))
                    queue.append([ni, nj, moves + 1, curKeys, keys])

        return -1
