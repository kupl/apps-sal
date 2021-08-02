# D - Number of Amidakuji

H, W, K = list(map(int, input().split()))
MOD = 10**9 + 7

comb = []


def dfs(n, p):
    if len(n) == (W - 1):
        if len(n) == 0:
            n = [0]
        comb.append(tuple(n))
        return
    for i in (0, 1):
        if p == 1 and i == 1:
            continue
        n.append(i)
        dfs(n, i)
        n.pop()


dfs([], 0)

dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1
for h in range(H):
    for w in range(W):
        # まっすぐ降りてくるケース
        tmp = 0
        for i in comb:
            if w == 0 and i[w] == 0:
                tmp += 1
            elif w == (W - 1) and i[w - 1] == 0:
                tmp += 1
            elif i[w - 1] == 0 and i[w] == 0:
                tmp += 1
        dp[h + 1][w] += dp[h][w] * tmp

        # 左からくるケース
        if w != 0:
            tmp = 0
            for i in comb:
                if i[w - 1] == 1:
                    tmp += 1
            dp[h + 1][w] += dp[h][w - 1] * tmp

        # 右からくるケース
        if w != (W - 1):
            tmp = 0
            for i in comb:
                if i[w] == 1:
                    tmp += 1
            dp[h + 1][w] += dp[h][w + 1] * tmp

print((dp[H][K - 1] % MOD))
