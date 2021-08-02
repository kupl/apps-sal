n = int(input())
a, b = 0, 0


def gi(): return list(map(int, input().split(' ')))


u, v = gi()
x, y = gi()
for _ in range(n - 1):
    p, q = gi()
    w = (x - u) * (q - y) - (y - v) * (p - x)
    if w < 0:
        a += 1
    else:
        b += 1
    u, v, x, y = x, y, p, q

print(min(a, b))
