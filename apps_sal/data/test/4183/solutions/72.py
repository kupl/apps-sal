import math
N = int(input())
lsT = []
for i in range(N):
    lsT.append(int(input()))
a = lsT[0]
for b in range(1,N):
    a = a*lsT[b] // math.gcd(a,lsT[b])
print(a)
