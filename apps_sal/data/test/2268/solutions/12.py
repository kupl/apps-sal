n, m = map(int, input().split())
s = input()

d = {}
for i in "abcdefghijklmnopqrstuvwxyz":
    d[i] = []

for j, l in enumerate(s):
    d[l].append(j)

for i in range(m):
    xi, yi = input().split()
    d[xi], d[yi] = d[yi], d[xi]

r = {}
for k, v in d.items():
    for pos in v:
        r[pos] = k

for l in sorted(r.items()):
    print(l[1], end="")

