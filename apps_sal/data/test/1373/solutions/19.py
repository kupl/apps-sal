(N, K) = list(map(int, input().split()))
p = 10 ** 9 + 7
(L_min, L_max) = (0, 0)
for i in range(K - 1, N + 1):
    L_min += i * (i + 1) // 2 - 1
    L_max += N * (N + 1) // 2 - (N - i - 1) * (N - i) // 2
ans = (L_max - L_min) % p
print(ans)
