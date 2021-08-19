(n, m, d) = list(map(int, input().split()))
c = list(map(int, input().split()))
sumc = 0
for elem in c:
    sumc += elem
if sumc + (m + 1) * (d - 1) < n:
    print('NO')
else:
    print('YES')
    ans = []
    x = n - sumc
    for i in range(m):
        if x > d - 1:
            for j in range(d - 1):
                ans.append(0)
            for j in range(c[i]):
                ans.append(i + 1)
            x -= d - 1
        elif x > 0:
            for j in range(x):
                ans.append(0)
            for j in range(c[i]):
                ans.append(i + 1)
            x = 0
        else:
            for j in range(c[i]):
                ans.append(i + 1)
    for j in range(x):
        ans.append(0)
    print(*ans)
