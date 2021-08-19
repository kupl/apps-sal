n = int(input())
xa = []
for i in range(n):
    xa.append([int(c) for c in input().split()])
xa.sort()
mn = 0
bn = 0
for i in range(n):
    if xa[i][0] < 0:
        mn += 1
    else:
        bn += 1
ma = min(2 * min(bn, mn) + 1, n)
total = 0
if bn >= mn:
    for i in range(ma):
        total += xa[i][1]
else:
    for i in range(n - ma, n):
        total += xa[i][1]
print(total)
