(h, w, k) = map(int, input().split())
mod = 10 ** 9 + 7
dp = [0] * w
dp[0] = 1
fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for _ in range(h):
    t = [0] * w
    for i in range(w):
        if i > 0:
            t[i] += dp[i - 1] * fib[i - 1] * fib[w - i - 1]
        t[i] += dp[i] * fib[i] * fib[w - i - 1]
        if i < w - 1:
            t[i] += dp[i + 1] * fib[i] * fib[w - i - 2]
        t[i] %= mod
    dp = t
print(dp[k - 1])
