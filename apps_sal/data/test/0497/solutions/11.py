n = int(input())
l = [*map(int, input().split())]
d = {}
for (i, e) in enumerate(l):
    d[e] = i
v = sorted(d.values())
res = 0
for (i, e) in enumerate(l):
    j = v[-1]
    if e == l[j]:
        j = v[-2]
    res = max(res, j - i)
print(res)
