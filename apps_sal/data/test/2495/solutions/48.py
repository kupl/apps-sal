# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n,*a = map(int,read().split())


for i in range(1,n):
    a[i] += a[i-1]

aa = a[:]

sgn = 1
r1 = 0
v = 0
for i in range(n):
    a[i] += v
    if sgn:
        if a[i] <= 0:
            r1 += -a[i]+1
            v += -a[i]+1
    else:    
        if a[i] >= 0:
            r1 += a[i]+1
            v -= a[i]+1
    sgn ^= 1
    

a = aa
sgn = 0
r2 = 0
v = 0
for i in range(n):
    a[i] += v
    if sgn:
        if a[i] <= 0:
            r2 += -a[i]+1
            v += -a[i]+1
    else:    
        if a[i] >= 0:
            r2 += a[i]+1
            v -= a[i]+1
    sgn ^= 1

#print(r1,r2)
print(min(r1,r2))
