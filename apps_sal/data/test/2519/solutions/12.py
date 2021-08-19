from itertools import accumulate
(N, K) = list(map(int, input().split()))
P = list(map(int, input().split()))
P = [(x + 1) * x / 2 / x for x in P]
A = list(accumulate(P))
ans = A[K - 1]
for i in range(K, N):
    ans = max(ans, A[i] - A[i - K])
print(ans)
