(n, m, a) = map(int, input().split())
(b, p) = (sorted(map(int, input().split())), sorted(map(int, input().split())))


def f(k):
    return sum((max(0, p[i] - b[n - k + i]) for i in range(k)))


def g(k):
    return sum((min(b[n - k + i], p[i]) for i in range(k)))


(x, y, d) = (0, min(n, m) + 1, a)
while y - x > 1:
    k = (x + y) // 2
    s = f(k)
    if s > a:
        y = k
    else:
        (x, d) = (k, s)
print(x, max(0, g(x) - a + d))
