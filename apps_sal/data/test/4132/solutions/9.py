from math import gcd

N = int(input())
A = list(map(int, input().split()))
min_ = 0
gcd_ = A[0]
for i in range(1, N):
    gcd_ = gcd(A[i], gcd_)
print(gcd_)
