n, a, b = map(int, input().split())
r = []


def f(a, l, r=r):
    r += [a + l - 1] + list(range(a, a + l - 1))


i = 1
while n > 0:
    if n % b is 0:
        break
    f(i, a)
    i += a
    n -= a
while n > 0:
    f(i, b)
    i += b
    n -= b
print(-1) if n else print(*r)
