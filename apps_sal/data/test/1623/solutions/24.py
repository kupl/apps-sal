(n, l, r) = map(int, input().split())
minx = 0
maxx = 0
for i in range(r):
    maxx += 2 ** i
maxx += 2 ** (r - 1) * (n - r)
for i in range(l):
    minx += 2 ** i
minx += 1 * (n - l)
print(minx, maxx)
