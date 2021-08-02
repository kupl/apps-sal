from math import atan2


def s(a, b): return a[0] * b[0] + a[1] * b[1]
def v(a, b): return a[0] * b[1] - a[1] * b[0]


p = []
for i in range(int(input())):
    x, y = map(int, input().split())
    p.append((atan2(x, y), (x, y), i + 1))
p.sort()

d = [(s(a, b), abs(v(a, b)), i, j) for (x, a, i), (y, b, j) in zip(p, p[1:] + p[:1])]
x = d[0]

for y in d:
    if v(y[:2], x[:2]) > 0:
        x = y

print(x[2], x[3])
