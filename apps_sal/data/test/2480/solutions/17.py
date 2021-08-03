from collections import Counter


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

S = [0] * (N + 1)
for i in range(N):
    # S[i + 1] = (S[i] + A[i]) % K
    S[i + 1] = S[i] + A[i]

cnt = 0
C = Counter()
for r in range(N + 1):
    R = (S[r] - r) % K
    cnt += C[R]
    C[R] += 1
    l = r - (K - 1)
    if l >= 0:
        L = (S[l] - l) % K
        C[L] -= 1

print(cnt)
