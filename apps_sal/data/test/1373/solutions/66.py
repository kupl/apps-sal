(N, K) = list(map(int, input().split()))
MOD = 10 ** 9 + 7
ac = [0] * (N + 1)
for i in range(1, N + 1):
    ac[i] = ac[i - 1] + i
ans = 1
for i in range(K, N + 1):
    r = ac[-1] - ac[N - i]
    l = ac[i - 1]
    ans += (r - l + 1) % MOD
print(ans % MOD)
