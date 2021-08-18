n, x = list(map(int, input().split()))
a = []
for i in range(x + 1):
    a.append([])
for i in range(n):
    L, R, C = list(map(int, input().split()))
    if R - L + 1 > x:
        continue
    a[R - L + 1].append([L, R, C])
for i in range(x + 1):
    a[i] = sorted(a[i])

ans = int(3e9 + 1)
for i in range(x + 1):
    m = int(3e9 + 1)
    z = 0
    for j in range(len(a[i])):
        while z != len(a[x - i]) and a[i][j][0] > a[x - i][z][1]:
            m = min(m, a[x - i][z][2])
            z += 1
        ans = min(ans, m + a[i][j][2])
if ans == int(3e9 + 1):
    print(-1)
else:
    print(ans)
