x, y = map(int, input().split())
mod = 10**9 + 7
if x // 2 + 2 * (x % 2) <= y <= 2 * x and (2 * x - y) % 3 == 0:
    t = (2 * x - y) // 3
    maxt = max(t, x - t)
    a = 1
    b = 1
    ans = 1
    for i in range(1, maxt + 1):
        a = a * (maxt - i + 1) % mod
        b = b * i % mod
        if i == t or i == x - t:
            ans *= a * pow(b, mod - 2, mod) % mod
    print(ans)
else:
    print(0)
