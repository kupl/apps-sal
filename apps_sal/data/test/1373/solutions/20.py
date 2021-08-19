(N, K) = map(int, input().split())
MOD = 10 ** 9 + 7
s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = s[i - 1] + i
ans = 0
for n in range(K, N + 2):
    mn = s[n - 1] - s[0]
    mx = s[N] - s[max(N - n, 0)]
    count = mx - mn + 1
    ans += count
    ans %= MOD
print(ans)
