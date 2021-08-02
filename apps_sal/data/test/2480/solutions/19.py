from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * (N + 1)
for i in range(N):
    B[i + 1] = (B[i] + A[i] - 1) % K
r = 0
d = defaultdict(int)
for i in range(N + 1):
    r += d[B[i]]
    d[B[i]] += 1
    if K - 1 <= i:
        d[B[i - K + 1]] -= 1
print(r)
