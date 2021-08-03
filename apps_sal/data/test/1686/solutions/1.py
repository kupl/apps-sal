def f(t):
    a, b, c, d = map(int, t.split('.'))
    return d + (c << 8) + (b << 16) + (a << 24)


def g(x):
    p = [0] * 4
    for i in range(4):
        p[3 - i] = str(x % 256)
        x //= 256
    return '.'.join(p)


n, k = map(int, input().split())
t = [f(input()) for i in range(n)]
p = [0] * n
x = 1 << 31
for i in range(32):
    for j, y in enumerate(t):
        if y & x:
            p[j] += x
    if len(set(p)) >= k:
        break
    x >>= 1
print(-1 if len(set(p)) != k else g((1 << 32) - x))
