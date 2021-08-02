# -*- coding: utf-8 -*-

H, W, K = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))

C = [input() for _ in range(H)]
T = [[-1 for _ in range(W)] for _ in range(H)]
T[x1 - 1][y1 - 1] = 0

que = {(x1 - 1, y1 - 1): 0}
step = 1

while len(que) > 0:
    que_next = {}
    for q in list(que.keys()):
        x, y = q[0], q[1]
        for i in range(1, K + 1):
            if x - i < 0:
                break
            if C[x - i][y] == '@' or T[x - i][y] == 1:
                break
            if x - i == x2 - 1 and y == y2 - 1:
                print(step)
                return
            que_next[(x - i, y)] = 0
        for i in range(1, K + 1):
            if x + i > H - 1:
                break
            if C[x + i][y] == '@' or T[x + i][y] == 1:
                break
            if x + i == x2 - 1 and y == y2 - 1:
                print(step)
                return
            que_next[(x + i, y)] = 0
        for i in range(1, K + 1):
            if y - i < 0:
                break
            if C[x][y - i] == '@' or T[x][y - i] == 1:
                break
            if x == x2 - 1 and y - i == y2 - 1:
                print(step)
                return
            que_next[(x, y - i)] = 0
        for i in range(1, K + 1):
            if y + i > W - 1:
                break
            if C[x][y + i] == '@' or T[x][y + i] == 1:
                break
            if x == x2 - 1 and y + i == y2 - 1:
                print(step)
                return
            que_next[(x, y + i)] = 0
    que = que_next
    for q in list(que.keys()):
        T[q[0]][q[1]] = 1
    step += 1

print((-1))
