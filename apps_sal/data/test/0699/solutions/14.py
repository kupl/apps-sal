"""
Created on Apr 27, 2016
Gmail : r.haque.249.rh@gmail.com
@author: Md. Rezwanul Haque
"""
import sys
'\nCreated on Apr 27, 2016\nGmail : r.haque.249.rh@gmail.com\n@author: Md. Rezwanul Haque\n'
f = sys.stdin
(y, k, n) = map(int, f.readline().strip().split())
if y >= n:
    first = -1
else:
    t = k
    while t <= y:
        t += k
    first = t - y
if first == -1:
    print(-1)
elif first + y > n:
    print(-1)
else:
    res = []
    for i in range(first, n + 1 - y, k):
        res.append(i)
    print(*res)
