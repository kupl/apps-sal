import math
N = int(input())
A = list(map(int, input().split()))
gcd = A[0]
for i in range(1, N):
    gcd = math.gcd(gcd, A[i])
print(gcd)
