import math

N, M = map(int,input().split())
A = list(map(int,input().split()))

pow2 = 0
while A[0] % 2 == 0:
    A[0] //= 2
    pow2 += 1

for i in range(1,N):
    cnt = 0
    while A[i] % 2 == 0:
        A[i] //= 2
        cnt += 1
    if cnt != pow2:
        print(0)
        return

LCM = 2**max(0,pow2-1)
for i in range(N):
    LCM = LCM * A[i] // math.gcd(LCM,A[i])

ans = M // LCM
print((ans+1)//2)
