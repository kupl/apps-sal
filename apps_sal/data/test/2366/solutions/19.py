from collections import Counter
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n=int(input())
a=list(map(int,input().split()))
c=Counter(a)
com=0
for i in range(1,n+1):
    if(c[i]<=1):
        continue
    com+=combinations_count(c[i],2)
for k in range(1,n+1):
    ans=com
    ans-=c[a[k-1]]-1
    print(ans)
