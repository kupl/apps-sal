H, W, D = map(int, input().split())
x = [0] * (H * W + 1)
for i in range(H):
    a = list(map(int, input().split()))
    for j in range(W):
        x[a[j]] = [i, j]

d = [0] * (H * W + 1)
for i in range(1, H * W + 1):
    if i > D:
        d[i] = d[i - D] + abs(x[i][0] - x[i - D][0]) + abs(x[i][1] - x[i - D][1])

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(d[r] - d[l])
