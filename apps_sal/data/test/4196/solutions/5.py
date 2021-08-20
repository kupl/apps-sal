from math import gcd
from functools import reduce


def gcd_list(numbers):
    return reduce(gcd, numbers)


N = int(input())
A = list(map(int, input().split()))
X = [0] * N
Y = [0] * N
X[0] = A[0]
Y[-1] = A[-1]
ans = [0] * N
for i in range(1, N):
    X[i] = gcd(X[i - 1], A[i])
    Y[N - i - 1] = gcd(Y[N - i], A[N - i - 1])
for i in range(1, N - 1):
    ans[i] = gcd(X[i - 1], Y[i + 1])
(ans[0], ans[-1]) = (gcd_list(A[1:]), gcd_list(A[:-1]))
print(max(ans))
