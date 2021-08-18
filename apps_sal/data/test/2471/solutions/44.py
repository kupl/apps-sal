from bisect import bisect_right
from bisect import bisect_left
H, W, N = list(map(int, input().split()))
matrix = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    matrix.append([x, y])
matrix.sort()
ans = [0 for _ in range(10)]
cand = {}
for l in matrix:
    for x_r in [-2, -1, 0]:
        for y_r in [-2, -1, 0]:
            nowx = l[0] + x_r
            nowy = l[1] + y_r
            if nowx < 0 or nowy < 0 or nowx + 2 >= H or nowy + 2 >= W:
                continue
            name = str(nowx) + ' ' + str(nowy)
            if name in cand:
                cand[name] += 1
            else:
                cand[name] = 1
tmp = ((H - 2) * (W - 2))
for x in list(cand.values()):
    ans[x] += 1
    tmp -= 1
ans[0] = tmp
for x in ans:
    print(x)
