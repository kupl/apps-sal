import re
import copy
import numpy as np
import queue


def accept_input():
    H, W = list(map(int, input().split()))
    S = []
    for _ in range(H):
        S.append(input())
    return H, W, S


def widthsearch(q):
    movelist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while not q.empty():
        pack = q.get()
        y = pack[0][0]
        x = pack[0][1]
        num = pack[1]
        if S[y][x] == "g":
            return num
        for move in movelist:
            if y + move[0] == -1 or y + move[0] == H or x + move[1] == -1 or x + move[1] == W:
                continue
            elif visitedlist[y + move[0]][x + move[1]] == 1:
                continue
            elif S[y + move[0]][x + move[1]] == "#":
                continue
            else:
                visitedlist[y + move[0]][x + move[1]] = 1
                q.put(((y + move[0], x + move[1]), num + 1))
    return -1


H, W, S = accept_input()
for i in range(len(S)):
    if i == 0:
        S[i] = "s" + S[i][1:]
    if i == H - 1:
        S[i] = S[i][:W - 1] + "g"
siro = H * W
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            siro -= 1
q = queue.Queue()
q.put(((0, 0), 0))
# 幅優先探索
visitedlist = np.zeros((H, W))
visitedlist[0][0] = 1
result = widthsearch(q)
if result == -1:
    print((-1))
else:
    print((siro - result - 1))
