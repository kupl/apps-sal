import sys
N, M = map(int, input().split())
L = list(map(int, input().split()))
if N >= M:
    print(0)
    return
L.sort()
K = []
s = 0
for i in range(M - 1):
    K.append(L[i + 1] - L[i])
K.sort(reverse=True)
for i in range(N - 1):
    s += K[i]
print(L[M - 1] - L[0] - s)
