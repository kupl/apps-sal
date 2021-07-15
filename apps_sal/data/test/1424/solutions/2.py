def f(n, a, b):
    cnt = 0
    now = 1
    for i in range(n):
        if a & now == b & now:
            cnt += 1
        now *= 2
    return cnt
n, m, k = map(int, input().split())
a = []
for i in range(m + 1):
    a.append(int(input()))
ans = 0
for i in range(m):
    if f(n, a[i], a[m]) >= n - k:
        ans += 1
print(ans)
