from itertools import accumulate
(N, K) = map(int, input().split())
acc = list(accumulate(range(N + 1), lambda x, y: x + y))
ans = 0
mod = 10 ** 9 + 7
for i in range(K, N + 1):
    r = acc[N] - acc[N - i]
    l = acc[i - 1]
    ans = (ans + r - l + 1) % mod
ans += 1
print(ans % mod)
