(n, k) = map(int, input().split())


def f(x):
    mi = max(1, x - n)
    ma = min(n, x - 1)
    return ma - mi + 1


ans = 0
for p in range(2, 2 * n + 1):
    q = p - k
    if q < 1 or q > 2 * n:
        continue
    ans += f(p) * f(q)
print(ans)
