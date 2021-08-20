import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
a = [tuple(map(int, input().split())) for i in range(n)]
q = [tuple(map(int, input().split())) for j in range(m)]
a.sort(key=lambda x: x[1], reverse=True)
rng = 5 * 10 ** 5 + 1
idx = 0
dbl = [[0] * rng for j in range(20)]
for i in range(rng)[::-1]:
    if i > a[0][1]:
        continue
    while idx <= n - 1 and i < a[idx][0]:
        idx += 1
    if idx == n:
        break
    if a[idx][0] <= i <= a[idx][1]:
        dbl[0][i] = a[idx][1]
for i in range(1, 20):
    for j in range(rng):
        dbl[i][j] = dbl[i - 1][dbl[i - 1][j]]
for (l, r) in q:
    if dbl[-1][l] < r:
        print(-1)
        continue
    ans = 0
    for i in range(20)[::-1]:
        if dbl[i][l] < r:
            ans += 2 ** i
            l = dbl[i][l]
    print(ans + 1)
