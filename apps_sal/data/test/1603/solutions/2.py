import sys
import itertools
f = sys.stdin
n = int(f.readline().strip())
v = [int(u) for u in f.readline().strip().split()]
m = int(f.readline().strip())
vs = list(itertools.accumulate(v))
u = sorted(v)
us = list(itertools.accumulate(u))
p = []
for i in range(m):
    (type, l, r) = list(map(int, f.readline().strip().split()))
    if type == 1:
        if l > 1:
            p.append(str(vs[r - 1] - vs[l - 2]))
        else:
            p.append(str(vs[r - 1]))
    elif l > 1:
        p.append(str(us[r - 1] - us[l - 2]))
    else:
        p.append(str(us[r - 1]))
print('\n'.join(p))
