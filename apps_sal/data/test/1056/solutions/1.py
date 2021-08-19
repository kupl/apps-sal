from math import *
c = 10
av = []
for i in range(c):
    l = [int(s) for s in input().split()]
    if i % 2 == 0:
        l.reverse()
    for j in range(c):
        if l[j] % 2 == 0:
            l[j] = c * l[j]
        else:
            l[j] = c * l[j] + c - 1 - 2 * j
    av = l + av
d = [0] * c ** 2
for i in range(c ** 2 - 2, -1, -1):
    rep = max(0, 6 - c ** 2 + 1 + i)
    t = 0
    for j in range(1, 6 - rep + 1):
        t += min(d[i + j], d[i + j + av[i + j]]) + 1
    d[i] = (rep + t) / (6 - rep)
print(d[0])
