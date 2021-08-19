import sys
n = int(input())
g = {'A': lambda a, b: v[a] & v[b], 'O': lambda a, b: v[a] | v[b], 'X': lambda a, b: v[a] ^ v[b], 'N': lambda a: v[a] ^ 1, 'I': lambda a: a + 1}


def f(q):
    q = q.split()
    return (q.pop(0)[0], [int(t) - 1 for t in q])


d = [f(q) for q in sys.stdin.readlines()]
t = [0]
for i in t:
    (f, a) = d[i]
    if f != 'I':
        t.extend(a)
v = [0] * n
for i in t[::-1]:
    (f, a) = d[i]
    v[i] = g[f](*a)
s = [0] * n
s[0] = 1
for i in t:
    if not s[i]:
        continue
    (f, a) = d[i]
    if f == 'I':
        continue
    for k in a:
        v[k] ^= 1
        s[k] = g[f](*a) != v[i]
        v[k] ^= 1
print(''.join((str(q ^ v[0]) for (q, (f, a)) in zip(s, d) if f == 'I')))
