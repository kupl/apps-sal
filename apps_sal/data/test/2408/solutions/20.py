from fractions import Fraction
from collections import Counter
n = int(input())

p = []

lines = set()
c = Counter()
for _ in range(n):
    x, y = list(map(int, input().split()))
    p.append((x, y))


for i in range(n - 1):
    for j in range(i + 1, n):
        try:
            l = (
                Fraction(p[i][1] - p[j][1], p[i][0] - p[j][0]),
                Fraction(p[j][1] * p[i][0] - p[i][1] * p[j][0], p[i][0] - p[j][0])
            )
        except ZeroDivisionError:
            l = ('i', p[i][0])
        if l not in lines:
            lines.add(l)
            c[l[0]] += 1

# print(lines)
# print(c)
# print(len(lines))

t = 0

tt = len(lines)
for l in lines:
    t += tt - c[l[0]]


print(t // 2)
