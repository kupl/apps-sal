l, a, b, m = map(int, input().split())

ten = 1


def f(x):

    if x == 0:
        return 0
    if x % 2 == 1:
        t = x - 1
        x = f(t)
        return x * ten + 1
    else:
        t = x // 2
        x = f(t)
        return x * pow(ten, t, m) + x


def g(x):

    if x == 0:
        return 0
    if x % 2 == 1:
        t = x - 1
        x = g(t)
        return x * ten + b * (t)
    else:
        t = x // 2
        x = g(t)
        return x * pow(ten, t, m) + x + b * (t) * f(t)


last = a + b * (l - 1)

ans = 0
for i in range(1, 20):
    le = ten
    r = ten * 10 - 1

    ten *= 10
    if last < le or a > r:
        continue
    if le < a:
        na = a
    else:
        na = (le - a + b - 1) // b * b + a
    if last <= r:
        nl = last
    else:
        nl = (r - a) // b * b + a
    n = (nl - na) // b + 1

    ans *= pow(ten, n, m)
    ans += ((f(n) % m) * na) % m
    ans += g(n) % m
    ans %= m

print(ans)
