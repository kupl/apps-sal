N, K = map(int, input().split())
RSP = list(map(int, input().split()))
T = input()

# dp[i][j]: i 回目に j を出したときの得点
# 0: グー, 1: チョキ, 2: パー
dp = [[0] * 3 for _ in range(N + 1)]


def judge(a, b):
    # パーで勝ったとき
    if a == 'r' and b == 2:
        return RSP[2]
    # グーで勝ったとき
    elif a == 's' and b == 0:
        return RSP[0]
    # チョキで勝ったとき
    elif a == 'p' and b == 1:
        return RSP[1]
    return 0


# i 回目のじゃんけん
for i in range(1, N + 1):
    # i 回目に出した手
    for j in range(3):
        # i-K 回目に出した手
        for k in range(3):
            # K 回前と同じ手を出したとき
            if j == k:
                continue
            # j を出したとき
            dp[i][j] = max(dp[i][j], dp[i - K][k] + judge(T[i - 1], j))

ans = 0
for k in range(K):
    ans += max(dp[N - k])
print(ans)
