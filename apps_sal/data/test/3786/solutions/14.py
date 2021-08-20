n = int(input())
a = [int(e) for e in input().split()]
d = {1: 0}
for (k, v) in enumerate(a):
    d[k + 2] = d[v] + 1
d2 = {}
for (k, v) in d.items():
    d2[v] = d2.get(v, 0) + 1
s = sum([v % 2 for v in d2.values()])
print(s)
