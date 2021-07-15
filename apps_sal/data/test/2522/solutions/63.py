# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, = list(map(int,readline().split()))
*a, = [2*int(x) for x in readline().split()]
*b, = [2*int(x)+1 for x in readline().split()]

c = sorted(a+b)
res = []
aa = []
bb = []
for x,y in zip(c[:n],c[n:]):
    if x%2 == 0:
        if y%2 == 0:
            aa.append((x//2,y//2))
        else:
            res.append((x//2,y//2))
    else:
        if y%2 == 0:
            res.append((y//2,x//2))
        else:
            bb.append((x//2,y//2))

while aa:
    p,q = aa.pop()
    r,s = bb.pop()
    if p != r and q != s:
        res.append((p,r))
        res.append((q,s))
    else:
        res.append((p,s))
        res.append((q,r))

from operator import itemgetter
res.sort(key = itemgetter(0))

for x,y in res:
    if x==y:
        print("No")
        return
print("Yes")
ans = [y for x,y in res]
print((*ans))



