from bisect import *
u, v = {}, {}
for q in range(int(input())):
    a, t, x = map(int, input().split())
    if x not in u: u[x], v[x] = [], []
    if a < 3: insort([v, u][-a][x], t)
    else: print(bisect(u[x], t) - bisect(v[x], t))
