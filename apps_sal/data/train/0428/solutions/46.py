from collections import deque


class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        keyMap = {ch: 1 << offset for (offset, ch) in enumerate('abcdef')}

        def hasKey(state, key):
            return state & keyMap[key]

        def setKey(state, key):
            return state | keyMap[key]
        keys = set()
        start = None
        target = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if 'a' <= grid[i][j] <= 'f':
                    target = setKey(target, grid[i][j])
                elif grid[i][j] == '@':
                    start = (i, j)

        def neighbors(i, j):
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for (di, dj) in moves:
                if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and (grid[i][j] != '#'):
                    yield (i + di, j + dj)
        visited = set()
        q = deque([[start, 0, 0]])
        while q:
            (coord, oldKeys, steps) = q.popleft()
            for n in neighbors(coord[0], coord[1]):
                newKeys = oldKeys
                c = grid[n[0]][n[1]]
                if 'A' <= c <= 'F' and (not hasKey(newKeys, c.lower())):
                    continue
                if 'a' <= c <= 'f':
                    newKeys = setKey(newKeys, c)
                if newKeys == target:
                    return steps + 1
                if (n, newKeys) not in visited:
                    visited.add((n, newKeys))
                    q.append([n, newKeys, steps + 1])
        return -1
