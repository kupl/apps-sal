(l, r, x, y) = map(int, input().split())


def f(ka, kb):
    return int(gcd(ka * x, kb * x) == x and l <= ka * x <= r and (l <= kb * x <= r))


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


cnt = 0
k = y // x
d = 1
while d * d <= k:
    if k % d == 0:
        cnt += f(d, k // d)
        if d * d != k:
            cnt += f(k // d, d)
    d += 1
if y % x:
    cnt = 0
print(cnt)
