from collections import deque
(H, W) = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())
yudlr = [-1, 1, 0, 0]
xudlr = [0, 0, -1, 1]
D = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        d = [[-1] * W for _ in range(H)]
        d[i][j] = 0
        Q = deque()
        Q.append([i, j])
        while len(Q) > 0:
            q = Q.popleft()
            (y, x) = (q[0], q[1])
            for k in range(4):
                y1 = y + yudlr[k]
                x1 = x + xudlr[k]
                if y1 < 0 or y1 >= H or x1 < 0 or (x1 >= W):
                    continue
                if S[y1][x1] == '#':
                    continue
                if d[y1][x1] != -1:
                    continue
                d[y1][x1] = d[y][x] + 1
                Q.append([y1, x1])
        Dij = max(list(map(lambda x: max(x), d)))
        D = max(D, Dij)
print(D)
