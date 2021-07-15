import sys
from collections import deque


def LI():
    return list(map(int, input().split()))


def LSH(h):
    return [list(input()) for _ in range(h)]


H, W = LI()
MAP = LSH(H)
d = deque()
d.append([0, 0])
looked = [[0 for i in range(W)]for j in range(H)]
looked[0][0] = 1
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
while d:
    x = d.popleft()
    h = x[0]
    w = x[1]
    for i in move:
        a = h+i[0]
        b = w+i[1]
        if not(0 <= a < H) or not(0 <= b < W) or looked[a][b] != 0 or MAP[a][b] == "#":
            continue
        d.append([a, b])
        looked[a][b] = looked[h][w]+1
if looked[H-1][W-1] == 0:
    print((-1))
    return

white = 0
for i in range(H):
    for j in range(W):
        if MAP[i][j] == ".":
            white += 1

print((white-looked[H-1][W-1]))

