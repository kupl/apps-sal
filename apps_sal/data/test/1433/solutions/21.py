(n, m) = list(map(int, input().split()))
ans = 0
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if a[i][j]:
            ans += a[i][j:].count(0)
            break
    for j in range(m - 1, -1, -1):
        if a[i][j]:
            ans += a[i][:j].count(0)
            break
for j in range(m):
    for i in range(n):
        if a[i][j]:
            for k in range(i, n):
                if a[k][j] == 0:
                    ans += 1
            break
    for i in range(n - 1, 0, -1):
        if a[i][j]:
            for k in range(i):
                if a[k][j] == 0:
                    ans += 1
            break
print(ans)
