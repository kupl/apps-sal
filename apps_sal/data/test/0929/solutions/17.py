import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
#mod = 998244353
INF = 10**18
eps = 10**-7

H, W = list(map(int, readline().split()))

a = [list(map(int, readline().split())) for i in range(H)]

ans = []

for i in range(H - 1):
    if i % 2:
        for j in range(W - 1, 0, -1):
            if a[i][j] % 2:
                ans.append((i + 1, j + 1, i + 1, j))
                a[i][j] -= 1
                a[i][j - 1] += 1
        if a[i][0] % 2:
            ans.append((i + 1, 1, i + 2, 1))
            a[i][0] -= 1
            a[i + 1][0] += 1

    else:
        for j in range(W - 1):
            if a[i][j] % 2:
                ans.append((i + 1, j + 1, i + 1, j + 2))
                a[i][j] -= 1
                a[i][j + 1] += 1
        if a[i][W - 1] % 2:
            ans.append((i + 1, W, i + 2, W))
            a[i][W - 1] -= 1
            a[i + 1][W - 1] += 1
if (H - 1) % 2:
    for j in range(W - 1, 0, -1):
        if a[H - 1][j] % 2:
            ans.append((H, j + 1, H, j))
            a[H - 1][j] -= 1
            a[H - 1][j - 1] += 1
else:
    for j in range(W - 1):
        if a[H - 1][j] % 2:
            ans.append((H, j + 1, H, j + 2))
            a[H - 1][j] -= 1
            a[H - 1][j + 1] += 1
print((len(ans)))
for (x, y, u, v) in ans:
    print((x, y, u, v))
