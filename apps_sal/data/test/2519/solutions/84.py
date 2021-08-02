from itertools import accumulate
N, K = map(int, input().split())
P = list(map(int, input().split()))

A = list(accumulate(P))

largest = A[K - 1]
point = 0
for i in range(K, N):
    if largest < A[i] - A[i - K]:
        largest = A[i] - A[i - K]
        point = i

ans = 0
for j in range(point - K + 1, point + 1):
    p = P[j]
    ans += (((p + 1) * p) / 2) / p

print(ans)
