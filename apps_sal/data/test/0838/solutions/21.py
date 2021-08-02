import math
def split(): return list(map(int, input().split()))


a, b = split()
rows = [split() for x in range(a)]
columns = [[x[y] for x in rows] for y in range(b)]


def choose(p, q):
    n = 1
    for x in range(p - q + 1, p + 1):
        n *= x
    n //= math.factorial(q)
    return n


s = 0
for x in rows + columns:
    p, q = x.count(0), x.count(1)
    for y in range(1, p + 1):
        s += choose(p, y)
    for y in range(1, q + 1):
        s += choose(q, y)
s -= a * b
print(s)
