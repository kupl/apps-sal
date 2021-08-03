N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
weight = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1] * (N + 1)
dp[0] = 0
for i in range(N + 1):  # dpで0~N本のマッチを探索
    for a in A:  # Aに入ってるもの（作れる数字）を探索
        if i + weight[a] < N + 1:  # i+(今回作る数字に必要なマッチ)本のマッチがN以下だったらOk
            dp[i + weight[a]] = max(dp[i + weight[a]], dp[i] *
                                    10 + a)
print((dp[N]))
