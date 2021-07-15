import math
N = int(input())
A = list(map(int,input().split()))
B = [0] * (N)
lcmall = A[0]
for i in range(1,N):
    gcdall = math.gcd(lcmall,A[i])
    lcmall = lcmall*A[i] // gcdall
sum = 0
for i in range(N):
    B[i] =int(lcmall // A[i])
    sum += B[i]
print(sum % (10 ** 9 + 7))
