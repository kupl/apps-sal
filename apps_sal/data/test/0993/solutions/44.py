from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))
D = defaultdict(int)


L = [0] * (N + 1)
D[0] += 1
for i in range(1, N + 1):
    L[i] = (L[i - 1] + A[i - 1]) % M
    D[L[i]] += 1
D = dict(D)
ans = 0
for v in D.values():
    if v > 1:
        ans += v * (v - 1) // 2
print(ans)
