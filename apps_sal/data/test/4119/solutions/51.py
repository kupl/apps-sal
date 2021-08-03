n, m = map(int, input().split())
x = list(map(int, input().split()))
ans = 0
if n < m:
    x.sort()
    l = [x[i + 1] - x[i] for i in range(m - 1)]
    l.sort()
    ans = max(x) - min(x)
    for i in range(n - 1):
        ans -= l[-1 - i]
print(ans)
