from collections import Counter
(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [0 for i in range(N + 1)]
for i in range(N):
    B[i + 1] += B[i] + A[i]
    B[i + 1] %= M
counterB = Counter(B)
ans = 0
for v in list(counterB.values()):
    ans += v * (v - 1) // 2
print(ans)
