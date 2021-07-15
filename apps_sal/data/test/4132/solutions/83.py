import math
N = int(input())
A = list(map(int,input().split()))
now = A[0]
for i in range(1,N):
    now = math.gcd(A[i],now)
print(now)

