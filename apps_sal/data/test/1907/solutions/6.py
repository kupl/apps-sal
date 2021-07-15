n = int(input())
d = [1] * n
p = [[] for i in range(n)]


def f():
    x, y, r = map(int, input().split())
    return r * r, x, y


t = sorted(f() for i in range(n))

for i in range(n):
    r, x, y = t[i]
    for j in range(i + 1, n):
        s, a, b = t[j]
        if (a - x) ** 2 + (b - y) ** 2 < s:
            p[j].append(i)
            d[i] = 0
            break


def f(i):
    s = t[i][0]
    q = [(1, j) for j in p[i]]
    while q:
        d, i = q.pop()
        s += d * t[i][0]
        q += [(-d, j) for j in p[i]]
    return s


print(3.1415926536 * sum(f(i) for i in range(n) if d[i]))
