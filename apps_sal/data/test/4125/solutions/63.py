from functools import reduce
from fractions import gcd

N, X = list(map(int, input().split()))
A = list(map(int,input().split()))

cnt  = []
for i in range(N):
    cnt.append(abs(X - A[i]))

print((reduce(gcd, cnt)))



