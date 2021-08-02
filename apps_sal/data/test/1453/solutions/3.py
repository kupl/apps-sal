n, m = [int(s) for s in input().split()]
t = [int(s) for s in input().split()]
t.sort()
g = [0] * m
tot = 0
for i in range(n):
    g[i % m] += t[i]
    tot += g[i % m]
    print(tot, end=' ')
