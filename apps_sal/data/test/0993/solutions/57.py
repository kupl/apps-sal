from collections import Counter
(N, M) = map(int, input().split())
A = list((int(a) for a in input().split()))
sumA = [0] * (N + 1)
for i in range(N):
    sumA[i + 1] = (sumA[i] + A[i]) % M
ans = 0
c = Counter(sumA)
for (k, v) in c.items():
    ans += v * (v - 1) // 2
print(ans)
