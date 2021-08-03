N, _ = map(int, input().split())
A = [int(i) for i in input().split()]

INF = "-"


def chmax(a: str, b: str):
    if a == INF:
        return b
    elif len(a) < len(b):
        return b
    elif len(a) == len(a):
        if a < b:
            return b
    return a


# 数字 : 必要なマッチの本数
cnt = dict(zip(range(1, 10), [2, 5, 5, 4, 5, 6, 3, 7, 6]))

# dp[i]: マッチをi本使って作れる数値の最大値
dp = [INF] * (10 ** 5)

# 初期条件
dp[0] = ""

# 配るDP
for i in range(N):
    if dp[i] == INF:
        continue
    for a in A:
        dp[i + cnt[a]] = chmax(dp[i + cnt[a]], dp[i] + chr(ord("0") + a))

print(dp[N])
