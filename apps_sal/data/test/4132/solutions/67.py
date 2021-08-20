from math import gcd
N = int(input())
A = list(map(int, input().split()))
res = 0
for i in range(N):
    res = gcd(res, A[i])
print(res)
