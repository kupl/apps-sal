from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

H, W, N = list(map(int, input().split()))
dic = defaultdict(int)
dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, 0, -1, -1, -1]
for i in range(N):
    y, x = list(map(int, input().split()))
    for j in range(9):
        ny, nx = y + dy[j], x + dx[j]
        if not 1 < ny < H:
            continue
        if not 1 < nx < W:
            continue
        dic[str(ny) + ":" + str(nx)] += 1
count = [0] * 10
tot = (H - 3 + 1) * (W - 3 + 1)
count[0] = tot - len(list(dic.keys()))
for k, v in list(dic.items()):
    count[v] += 1
for c in count:
    print(c)
