(N, K) = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
for k in range(K, N + 2):
    mx = k * (2 * N - k + 1) / 2
    mi = k * (k - 1) / 2
    add = mx - mi + 1
    ans += add
    ans %= mod
print(int(ans))
