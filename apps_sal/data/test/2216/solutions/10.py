# -*- coding: utf-8 -*-
import sys
f = sys.stdin
#f = open('H:\\Portable Python 3.2.5.1\\test_248B1.txt')
n, m, k = map(int, f.readline().strip().split())


ki = 1
ps = []
l = 0
p = []
for i in range(1, n + 1):
    if i % 2 == 0:
        r = range(m, 0, -1)
    else:
        r = range(1, m + 1)
    for j in r:
        p.append(str(i))
        p.append(str(j))
        l += 1
        if ki < k and l == 2:
            ps.append('2 ' + ' '.join(p))
            l = 0
            p = []
            ki += 1
ps.append(str(l) + ' ' + ' '.join(p))

print('\n'.join(ps))
