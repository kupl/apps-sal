#
a,b,q=list(map(int, input().split()))
*s,=[-10**11]+[int(input()) for _ in range(a)]+[10**11]
*t,=[-10**11]+[int(input()) for _ in range(b)]+[10**11]
*x,=[int(input()) for _ in range(q)]
s.sort()
t.sort()

from bisect import bisect_left
from itertools import product
for xi in x:
    ans=10**11
    i=bisect_left(s,xi)
    j=bisect_left(t,xi)
    for u,v in product(s[i-1:i+1],t[j-1:j+1]):
        d=min(abs(u-xi),abs(v-xi))+abs(u-v)####この式が簡明
        ans=min(d,ans)
    print(ans)
    


