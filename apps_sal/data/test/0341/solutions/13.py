# D - Prediction and Restriction
N,K = map(int,input().split())
score = list(map(int,input().split()))
T = input()

# dp[i][j]: i回目のじゃんけんで j を出したときの最大の合計点数
# グー: 0, チョキ: 1, パー: 2
dp = [[0]*3 for _ in range(N+1)]

def judge(a,b):
    # パーで勝つとき
    if a == 'r' and b == 2:
        return score[2]
    # グーで勝つとき
    elif a == 's' and b == 0:
        return score[0]
    # チョキで勝つとき
    elif a == 'p' and b == 1:
        return score[1]
    return 0
    
# i 回目のじゃんけん
for i in range(1,N+1):
    # i回目のじゃんけんで j を出したとき
    for j in range(3):
        # i-K 回目のじゃんけんで k を出したとき
        for k in range(3):
            # i = K 回以上のとき
            if i > K:
                # K 回前と同じ手を出したらスルー
                if j == k:
                    continue
            # i < K 回のとき
            else:
                # 勝ち続けるのが最適
                dp[i][j] = judge(T[i-1],j)
                continue
            # K 回前に k を出したときの得点に、j を出して得た得点を加点
            dp[i][j] = max(dp[i][j],dp[i-K][k] + judge(T[i-1],j))

ans = 0
for a in dp[-K:]:
    ans += max(a)
print(ans)
