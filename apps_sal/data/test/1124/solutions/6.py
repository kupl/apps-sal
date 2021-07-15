import math
N=int(input())
A=[int(x) for x in input().split()]
ans=A[0]
for i in range(1,N):
    ans=math.gcd(ans,A[i])
print(ans)
