import sys
N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 2:
    print(N - 1)
    return

if N % K == 0:
    print((len(A) - 1) // (K - 1))
else:
    print((len(A) - 1) // (K - 1) + 1)
