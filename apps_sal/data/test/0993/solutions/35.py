from collections import *
(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = (S[i] + A[i]) % M
c = Counter()
ans = 0
for i in range(N + 1):
    ans += c[S[i]]
    c[S[i]] += 1
print(ans)
