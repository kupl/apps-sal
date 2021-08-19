from collections import Counter
(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
S = [0] * (N + 1)
for (i, a) in enumerate(A):
    S[i + 1] = (S[i] + a - 1) % K
C = Counter()
ans = 0
for j in range(1, N + 1):
    C[S[j - 1]] += 1
    if j - K >= 0:
        C[S[j - K]] -= 1
    ans += C[S[j]]
print(ans)
