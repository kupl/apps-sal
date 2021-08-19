import sys
f = sys.stdin
n = int(f.readline().strip())
A = []
F = {}
for k in range(n):
    t = list(map(int, f.readline().strip().split()))
    A.append(t)
    if t[0] in F:
        F[t[0]] += 1
    else:
        F[t[0]] = 1
res = ''
p = []
for u in A:
    if u[1] in F:
        p.append(str(n - 1 + F[u[1]]) + ' ' + str(n - 1 - F[u[1]]))
    else:
        p.append(str(n - 1) + ' ' + str(n - 1))
print('\n'.join(p))
