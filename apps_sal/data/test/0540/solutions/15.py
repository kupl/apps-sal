import heapq
from copy import deepcopy
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def decr(x): return x - 1


H, W = list(map(int, input().split()))
l = [list(input()) for i in range(H)]
si, sj = list(map(decr, list(map(int, input().split()))))
gi, gj = list(map(decr, list(map(int, input().split()))))

que = []
heapq.heappush(que, (si, sj))
res = False
while len(que):
    i, j = heapq.heappop(que)
    for k in range(4):
        ni = i + dir[k][0]
        nj = j + dir[k][1]
        if ni == gi and nj == gj and l[ni][nj] == 'X':
            res = True
        if 0 <= ni < H and 0 <= nj < W and l[ni][nj] == '.':
            l[ni][nj] = 'X'
            heapq.heappush(que, (ni, nj))


if res:
    print("YES")
else:
    print("NO")
