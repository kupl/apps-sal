n = int(input())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
MAXANS = 300000010
f = {1: [c[i] for i in range(n)], 2: [MAXANS for _ in range(n)], 3: [MAXANS for _ in range(n)]}
v = [False for _ in range(n)]
l = 2
for i in range(n - 1):
    if v[i]:
        continue
    for j in range(i + 1, n):
        if a[j] > a[i] and c[j] > c[i]:
            v[j] = True
        if a[i] < a[j] and f[l - 1][i] + c[j] < f[l][j]:
            f[l][j] = f[l - 1][i] + c[j]
l = 3
for i in range(n - 1):
    if f[2][i] == MAXANS:
        continue
    for j in range(i + 1, n):
        if a[i] < a[j] and f[l - 1][i] + c[j] < f[l][j]:
            f[l][j] = f[l - 1][i] + c[j]
ans = min(f[3])
if ans == MAXANS:
    print(-1)
else:
    print(ans)
