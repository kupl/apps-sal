import sys
n = int(input())
f = {'AND': (lambda a, b: a & b), 'OR': (lambda a, b: a | b), 'XOR': (lambda a, b: a ^ b), 'NOT': (lambda a: a ^ 1)}
g = {'0': (lambda: 0), '1': (lambda: 1)}
d = [(g[v[0]], []) if o == 'IN' else (f[o], [int(a) - 1 for a in v]) for o, *v in map(str.split, sys.stdin.read().strip().split('\n'))]
t = [0]
for i in t:
    t.extend(d[i][1])
v = [0] * n
for i in t[::-1]:
    v[i] = d[i][0](*(v[x] for x in d[i][1]))
f = [0] * n
f[0] = 1
for i in t:
    if f[i] < 1:
        continue
    o, a = d[i]
    for k in a:
        v[k] ^= 1
        f[k] = (o(*(v[x] for x in a)) != v[i])
        v[k] ^= 1
print(''.join(str(f[i] ^ v[0]) for i in range(n) if not d[i][1]))
