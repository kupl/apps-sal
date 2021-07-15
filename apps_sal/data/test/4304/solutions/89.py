from itertools import accumulate
import sys
a,b=map(int,input().split())
n = 500000
l=[]
for i in range(n):
    l.append(i)
    tmp = sum(l)
    if abs(abs(a+tmp) - abs(b+tmp)) == i:
        print(tmp -b)
        return
