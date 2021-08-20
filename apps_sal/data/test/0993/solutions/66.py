from collections import defaultdict
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * N
B[0] = A[0] % M
C = defaultdict(int)
for i in range(1, N):
    B[i] = (B[i - 1] + A[i]) % M
for b in B:
    C[b] += 1
ans = C[0]
for key in C.keys():
    t = C[key]
    ans += t * (t - 1) // 2
print(ans)
