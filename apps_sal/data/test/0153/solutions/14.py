n, k, m = list(map(int, input().split()))
t = sorted(map(int, input().split()))

res = 0
for x in range(min(n, m // sum(t)) + 1):
    mm = m - x * sum(t)
    r = x * (k + 1)
    for i, ti in enumerate(t):
        div = min(mm // ti, n - x)
        mm -= div * ti
        r += div if i < k - 1 else div * 2
    res = max(res, r)
print(res)
