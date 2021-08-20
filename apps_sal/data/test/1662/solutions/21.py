import sys
import math
n = int(sys.stdin.readline())
an = [int(x) for x in sys.stdin.readline().split()]
d = dict()
for i in an:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
t = list(d.keys())
t.sort(reverse=True)
resr = []
resl = []
c = 1
resr.append(str(t[0]))
for i in t[1:]:
    if d[i] > 1:
        c += 2
        resr.append(str(i))
        resl.append(str(i))
    else:
        c += 1
        resr.append(str(i))
k = list(resl[::-1])
k.extend(resr)
print(c)
print(' '.join(k))
