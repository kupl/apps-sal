(H, W, K) = map(int, input().split())
mod = 10 ** 9 + 7
dp = W * [0]
dp[0] = 1
fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for h in range(H):
    t = W * [0]
    for w in range(W):
        if 0 < w:
            t[w] += dp[w - 1] * fib[w - 1] * fib[W - w - 1]
        t[w] += dp[w] * fib[w] * fib[W - w - 1]
        if w < W - 1:
            t[w] += dp[w + 1] * fib[w] * fib[W - w - 2]
        t[w] %= mod
    dp = t
print(dp[K - 1])
