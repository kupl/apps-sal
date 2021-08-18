from collections import *
H, W = map(int, input().split())
S = [(W + 2) * ["
S[1][1] = 1
Q = deque([[1, 1]])
D = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while Q:
    x, y = Q.popleft()
    for dx, dy in D:
        if S[x + dx][y + dy] == ".":
            S[x + dx][y + dy] = S[x][y] + 1
            Q.append([x + dx, y + dy])

if S[H][W] == ".":
    print(-1)
else:
    print((H + 2) * (W + 2) - sum(s.count("
