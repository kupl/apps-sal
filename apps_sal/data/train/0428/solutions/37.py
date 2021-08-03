class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        from collections import deque
        start = [0, 0]
        numofKeys = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = [i, j]
                if grid[i][j].isalpha():
                    numofKeys += 1
        numofKeys //= 2
        keys = 0
        visited = set()
        stack = deque([[start[0], start[1], 0, 0]])
        while stack:
            # print(stack)
            i, j, keys, count = stack.popleft()
            for a, b in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= a < m and 0 <= b < n:
                    if grid[a][b].isalpha() and ord('a') <= ord(grid[a][b]) <= ord('f'):
                        newkeys = keys | (1 << (ord(grid[a][b]) - ord('a')))
                    elif grid[a][b].isalpha() and keys & (1 << (ord(grid[a][b]) - ord('A'))):
                        newkeys = keys
                    elif grid[a][b].isalpha() or grid[a][b] == '#':
                        continue
                    else:
                        newkeys = keys

                    if newkeys == 2**numofKeys - 1:
                        return count + 1
                    elif (a, b, newkeys) in visited:
                        continue
                    else:
                        visited.add((a, b, newkeys))
                        stack.append((a, b, newkeys, count + 1))
        return -1
