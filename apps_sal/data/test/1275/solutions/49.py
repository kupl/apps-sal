(N, K) = map(int, input().split())
P = []
for i in range(2 * N + 1):
    P.append(min(i - 1, 2 * N + 1 - i))
ans = 0
for i in range(2, 2 * N + 1):
    if 2 <= i - K <= 2 * N:
        ans += P[i] * P[i - K]
print(ans)
