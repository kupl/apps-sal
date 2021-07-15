from collections import deque

x0, y0, x1, y1 = list(map(int, input().split()))
n = int(input())

bars = {}
for i in range(n):
    r, a, b = list(map(int, input().split()))
    if r not in bars:
        bars[r] = {}
    for j in range(a, b+1):
        bars[r][j] = -1

bars[x0][y0] = 0
q = deque()
q.append(tuple([x0, y0]))

while q:
    node = q.popleft()

    for i in range(-1, 2):
        row = node[0] + i
        if row not in bars:
            continue

        for j in range(-1, 2):
            col = node[1] + j
            if col not in bars[row] or (i == 0 and j == 0):
                continue

            if bars[row][col] == -1:
                bars[row][col] = bars[node[0]][node[1]] + 1
                q.append(tuple([row, col]))

    if bars[x1][y1] != -1:
        break

print(bars[x1][y1])

