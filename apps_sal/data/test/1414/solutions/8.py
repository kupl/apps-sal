import sys
n, m = list(map(int, input().split()))
m += 1
d = {'I': 0, 'M': 1, 'A': 2, 'D': 3, '\n': -7}
t = list(map(d.get, sys.stdin.read())) + [-7] * m
p = [[] for q in t]
c = [0] * len(t)
for a in range(n * m):
    for b in (a - m, a + m, a - 1, a + 1):
        if abs(t[b] - t[a] + 1) == 2:
            p[a].append(b)
            c[b] += 1
s = [i for i, q in enumerate(c) if not q]
while s:
    a = s.pop()
    for b in p[a]:
        t[b] = max(t[b], t[a] + 1)
        c[b] -= 1
        if c[b] == 0:
            s.append(b)
k = max(t) - 2 >> 2
print('Poor Inna!' if any(c) else k if k > 0 else 'Poor Dima!')
