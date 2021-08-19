(h, w, d) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
Q = int(input())
lis = [0] * (h * w)
for i in range(h):
    for j in range(w):
        lis[a[i][j] - 1] = (i, j)
cum = [0] * d
for i in range(d, h * w):
    cum.append(cum[i - d] + abs(lis[i][0] - lis[i - d][0]) + abs(lis[i][1] - lis[i - d][1]))
for i in range(Q):
    (l, r) = map(int, input().split())
    print(cum[r - 1] - cum[l - 1])
