#70
from math import gcd
n=int(input())
t=[int(input()) for i in range(n)]

ans=1
for i in range(n):
    ans*=t[i]//gcd(ans,t[i])
print(ans)

