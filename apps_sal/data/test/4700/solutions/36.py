n, m = list(map(int, input().split()))
h = [int(s) for s in input().split()]
ab = []

for i in range(m):
    ab.append([int(s) for s in input().split()])

h2 = []
for p in ab:
    if h[p[0] - 1] <= h[p[1] - 1]:
        h2.append(p[0] - 1)
    if h[p[0] - 1] >= h[p[1] - 1]:
        h2.append(p[1] - 1)

print((len(h) - len(list(set(h2)))))
