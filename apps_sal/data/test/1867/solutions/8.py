N = int(input())
a = [int(i) for i in input().split()]
d = {}
b = {}
for (i, f) in enumerate(a):
    if f not in d:
        d[f] = 0
        b[f] = [i, i]
    d[f] += 1
    b[f][1] = i
mn = max(d.values())
m = [0, N]
for k in list(d.keys()):
    if d[k] != mn:
        continue
    if b[k][1] - b[k][0] < m[1] - m[0]:
        m = b[k]
print(m[0] + 1, m[1] + 1)
