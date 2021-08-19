from bisect import bisect_left
(h, w, d) = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]
arys = [[] for i in range(d)]
sumarys = [[0] for i in range(d)]
biarys = [[] for i in range(d)]
for i in range(h):
    for j in range(w):
        x = a[i][j] % d
        arys[x].append((a[i][j], i, j))
for i in range(d):
    arys[i].sort(key=lambda x: x[0])
    tmp = 0
    (y, pi, pj) = arys[i][0]
    biarys[i].append(y)
    for j in range(1, len(arys[i])):
        (y, ni, nj) = arys[i][j]
        biarys[i].append(y)
        tmp += abs(pi - ni) + abs(pj - nj)
        sumarys[i].append(tmp)
        (pi, pj) = (ni, nj)
for (l, r) in lr:
    x = l % d
    li = bisect_left(biarys[x], l)
    ri = bisect_left(biarys[x], r)
    print(sumarys[x][ri] - sumarys[x][li])
