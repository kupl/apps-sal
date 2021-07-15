# -*- coding: utf-8 -*-

n = int(input())
a, b = [], []
for i in range(n):
    x, y = list(map(int, input().split()))
    a.append(x)
    b.append(y)
    
p = q = 0
c = 0
while c < n:
    if a[p] < b[q]:
        #print('{}<{}'.format(a[p], a[q]))
        p += 1
    else:
        #print('{}>{}'.format(a[p], a[q]))
        q += 1
    c += 1

p0 = max(p, n//2)
print('1'*p0 + '0'*(n-p0))
q0 = max(q, n//2)
print('1'*q0 + '0'*(n-q0))

