h, w, K = list(map(int, input().split()))


def two(x):
    return "0" * (w - 1 - len(bin(x)[2:])) + bin(x)[2:]


dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1
mod = 10**9 + 7
for i in range(h):
    for j in range(2**(w - 1)):
        r = two(j)
        f = 1
        for k in range(w - 2):
            if r[k] == r[k + 1] == "1":
                f = 0
                break
        if f:
            for k in range(w):
                if k + 1 < w:
                    if r[k] == "1":
                        dp[i + 1][k + 1] += dp[i][k]
                        dp[i + 1][k + 1] %= mod
                        continue
                if k > 0:
                    if r[k - 1] == "1":
                        dp[i + 1][k - 1] += dp[i][k]
                        dp[i + 1][k - 1] %= mod
                        continue
                dp[i + 1][k] += dp[i][k]
                dp[i + 1][k] %= mod
print((dp[h][K - 1]))
