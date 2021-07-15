from sys import *
t = list(map(int, stdin.read().split()))
p = [t[i + 1] * t[i] ** 2 for i in range(1, len(t), 2)]
k = {v: j for j, v in enumerate(sorted(set(p)))}
d = [0] * (len(k) + 1)
for v in p: 
    j = k[v]
    i = j + 1
    q = 0
    while j > 0:
        q = max(d[j], q)
        j -= j & -j
    q += v
    while i < len(d):
        d[i] = max(d[i], q)
        i += i & -i
print(max(d) * 3.14159265)
