import math,sys,re,itertools,pprint,collections,copy
rs,ri,rai,raf=input,lambda:int(input()),lambda:list(map(int, input().split())),lambda:list(map(float, input().split()))

n, n1, n2 = rai()
a = rai()
a.sort(reverse=True)

if n1 < n2:
    print(sum(a[:n1])/n1 + sum(a[n1:n1+n2])/n2)
else:
    print(sum(a[:n2])/n2 + sum(a[n2:n2 + n1])/n1)

