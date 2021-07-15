N = int(input())
A = [int(s) for s in input().split(' ')]

d = dict()
d2 = dict()
d3 = dict()
d4 = dict()
for a in A:
    d[a] = d.get(a, 0) + 1
for a in list(d.keys()):
    d2[a] = d[a] * (d[a] - 1) // 2
    d3[a] = (d[a] - 1) * (d[a] - 2) // 2
total = sum(d2[a] for a in list(d.keys()))

for a in A:
    print((total - d2[a] + d3[a]))




