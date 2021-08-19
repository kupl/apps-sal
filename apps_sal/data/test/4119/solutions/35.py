(n, m) = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
res = []
for i in range(m - 1):
    res.append(x[i + 1] - x[i])
res.sort()
ans = 0
for i in range(m - n):
    ans += res[i]
print(ans)
