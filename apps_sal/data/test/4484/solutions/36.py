import math
N,M = map(int,input().split())
if abs(N-M) > 1:
    print(0)
    return

fac = 1
num = 10**9 + 7
for i in range(1,N+1):
    fac *= i
    if fac > num:
        fac %= num

fac2 = 1
for i in range(1,M+1):
    fac2 *= i
    if fac2 > num:
        fac2 %= num

if N == M:
    print(fac**2*2%num)
else:
    print(fac*fac2%num)
