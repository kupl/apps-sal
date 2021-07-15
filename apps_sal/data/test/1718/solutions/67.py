import math
N, K = map(int, input().split())
A = list(map(int, input().split()))

if N == K:
    print(1)
    return

mi = 0
for i in range(N):
    if A[i] == 1:
        mi = i
        break

mc = N
for i in range(K):
    c = 1
    if mi - i > 0:
        c += math.ceil((mi - i) / (K-1))
    if mi + K - 1 - i < N:
        c += math.ceil((N - (mi + K - 1 - i) - 1) / (K - 1))
    if c < mc:
        mc = c
print(mc)
