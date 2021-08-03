import math
f = 998244353


def calc(a, b):
    m = max(a, b)
    n = min(a, b)

    t = 1
    p = 1
    for i in range(0, n):
        p *= (n - i) * (m - i)
        p //= i + 1
        t += p
    t = t % f
    return(t)


a, b, c = map(int, input().split())
ans = calc(a, b) * calc(b, c) * calc(c, a) % f
print(ans)
