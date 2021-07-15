import math
import sys
n=int(input())
a=[];b=[];g=0
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    a.append(x)
    b.append(y)
    g=math.gcd(g,x*y)
for i in range(n):
    if math.gcd(g,a[i])>1:
        g=math.gcd(g,a[i])
    else:
        g=math.gcd(g,b[i])
if g==1:
    print(-1)
else:
    print(g)
