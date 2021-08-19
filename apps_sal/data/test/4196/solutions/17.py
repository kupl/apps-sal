from math import gcd
N = int(input())
A = list(map(int, input().split()))
(L, R) = ([0], [0])
for i in range(N - 1):
    L += [gcd(L[i], A[i])]
    R += [gcd(R[i], A[-i - 1])]
print(max((gcd(L[i], R[-i - 1]) for i in range(N))))
