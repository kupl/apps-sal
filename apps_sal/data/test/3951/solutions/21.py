def gcd(a,b):
    if b==0: return a 
    return gcd(b,a%b)
n=int(input())
from collections import Counter 
l=[int(i) for i in input().split()]
g=Counter(l)
ans=[]

while g:
    m=max(g)
    g[m]-=1 
    for i in ans:
        g[gcd(m,i)]-=2 
    ans+=[m]
    g+=Counter()
print(*ans)

