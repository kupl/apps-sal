A,B=map(float,input().split())
from math import ceil
c = ceil(A/0.08)
d=ceil(B/0.1)
if c==d:
    print(c)
elif c<d and d < ceil((A+1)/0.08):
    print(d)
elif d<c and c < ceil((B+1)/0.1):
    print(c)
else:
    print(-1)
