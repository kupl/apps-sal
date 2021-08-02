n = int(input())
d = {}
for i in range(1, n + 1):
    d[i] = [*map(int, input().split())]

u = n - 1
c1 = 1
a, b = d[c1]
if b in d[a]:
    c2 = a
else:
    c2 = b


def p(x): return print(x, end=' ')


p(c1)
while u > 0:
    p(c2)
    (c3,) = set(d[c1]).intersection(set(d[c2]))
    c2, c1 = c3, c2
    u -= 1
