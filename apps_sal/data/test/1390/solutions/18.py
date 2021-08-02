n, m = map(int, input().split())
f = list(map(int, input().split()))
f.sort()
ans = f[m - 1] - f[0]
for i in range(m - n + 1):
    if ans > f[i + n - 1] - f[i]:
        ans = f[i + n - 1] - f[i]
print(ans)
