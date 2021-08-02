from collections import defaultdict

n, depth = [int(x) for x in input().split(' ')]
l = []
s = defaultdict(int)
b = defaultdict(int)
sl = []
bl = []
for i in range(n):
    d, p, q = [x for x in input().split(' ')]
    p = int(p)
    q = int(q)
    if d == 'S': s[p] += q
    else: b[p] += q

for p, q in list(s.items()): sl += [(p, q)]
for p, q in list(b.items()): bl += [(p, q)]

sl.sort()
bl.sort()
sp = ["S {0} {1}".format(i[0], i[1]) for i in sorted(sl[0:depth], key=lambda x: -x[0])]
bp = ["B {0} {1}".format(i[0], i[1]) for i in bl[-1:-depth - 1:-1]]

for i in (sp + bp): print(i)
