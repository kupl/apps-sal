import sys

lines = sys.stdin.read().split("\n")
# n, k = map(int, lines[0].split(" "))
# n = int(lines[0])
# nums = list(map(int, lines[1].split(" ")))


n, m = list(map(int, lines[0].split(" ")))
gra1 = []
for i in range(n + 1):
    gra1.append(set())
gra2 = [0] * (n + 1)

edges = []
for i in range(1, m + 1):
    a, b = list(map(int, lines[i].split(" ")))
    gra1[a].add(b)
    gra1[b].add(a)
    edges.append((a, b))

for i in range(1, n + 1):
    gra2[i] = len(gra1[i])

res = []
for edge in edges:
    a, b = edge
    tmp = gra2[a] + gra2[b]
    neighs = gra1[a].intersection(gra1[b])
    if len(neighs) <= 0:
        continue
    best = float("inf")
    for c in list(neighs):
        if gra2[c] < best:
            best = gra2[c]
    res.append(tmp + best)
res.sort()
if len(res) <= 0:
    print("-1")
else:
    print(res[0] - 6)
