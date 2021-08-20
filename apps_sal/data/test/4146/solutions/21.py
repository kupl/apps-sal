n = int(input())
V = list(map(int, input().split()))
d = {}
for i in range(0, n, 2):
    d[V[i]] = d.get(V[i], 0) + 1
m1 = 0
o = 0
o2 = 0
for i in d:
    if m1 <= d[i]:
        m1 = d[i]
        o = i
d[o] = 0
m2 = -1
for i in d:
    if m2 <= d[i]:
        m2 = d[i]
        o2 = i
d = {}
for i in range(1, n, 2):
    d[V[i]] = d.get(V[i], 0) + 1
m3 = 0
e = 0
e2 = 0
for i in d:
    if m3 <= d[i]:
        m3 = d[i]
        e = i
d[e] = 0
m4 = -1
for i in d:
    if m4 <= d[i]:
        m4 = d[i]
        e2 = i
if e != o:
    print(n - m1 - m3)
else:
    print(min(n - m1 - m4, n - m2 - m3))
