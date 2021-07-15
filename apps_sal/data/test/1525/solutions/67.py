from functools import lru_cache

H, W, K = map(int, input().split())
MOD = 10**9 + 7
K -= 1

if W == 1:
    print(1)
    return

@lru_cache(maxsize=None)
def fib(width):
    if width < -1:
        return 0
    if width == -1:
        return 1
    return (fib(width - 1) + fib(width - 2)) % MOD

dp = [0] * W
dp[0] = 1

for _ in range(H):
    newDp = [0] * W

    newDp[0] = (dp[0] * fib(W - 2) + dp[1] * fib(W - 3)) % MOD
    newDp[W - 1] = (dp[W - 1] * fib(W - 2) + dp[W - 2] * fib(W - 3)) % MOD

    for w in range(1, W - 1):
        left = dp[w - 1] * max(1, fib(w - 2)) * max(1, fib(W - 1 - w - 1))
        right = dp[w + 1] * max(1, fib(w - 1)) * max(1, fib(W - 1 - w - 2))
        mid = dp[w] * max(1, fib(w - 1)) * max(1, fib(W - 1 - w - 1))
        newDp[w] = (left + mid + right) % MOD
    dp = newDp

print(dp[K])
