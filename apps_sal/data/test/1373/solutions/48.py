(N, K) = map(int, input().split())
tmp = [0 for _ in range(10 ** 5 * 3 + 1)]
for i in range(10 ** 5 * 3):
    tmp[i + 1] = tmp[i] + (i + 1)
ans = 1
for i in range(K, N + 1):
    tmp_max = tmp[N] - tmp[N - i]
    ans += tmp_max - tmp[i - 1] + 1
print(ans % (10 ** 9 + 7))
