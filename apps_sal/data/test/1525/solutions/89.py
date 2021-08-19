import itertools
mod = 1000000007
(h, w, k) = list(map(int, input().split()))
dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1
for h_ in range(1, h + 1):
    for bridges in itertools.product([0, 1], repeat=w - 1):
        flag = 0
        for j in range(len(bridges) - 1):
            if bridges[j] == 1 and bridges[j + 1] == 1:
                flag = 1
                continue
        if flag == 1:
            continue
        for w_ in range(w):
            if w_ > 0:
                if bridges[w_ - 1] == 1:
                    dp[h_][w_] += dp[h_ - 1][w_ - 1] % mod
                    continue
            if w_ < w - 1:
                if bridges[w_] == 1:
                    dp[h_][w_] += dp[h_ - 1][w_ + 1] % mod
                    continue
            dp[h_][w_] += dp[h_ - 1][w_] % mod
print(dp[-1][k - 1] % mod)
