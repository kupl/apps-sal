from collections import defaultdict
N, A = map(int, input().split())
X = list(map(int, input().split()))

dp = defaultdict(dict)
dp[0][0] = 1  # カード0枚で合計

for x in X:
    newDP = defaultdict(dict)
    for card, memo in dp.items():
        for k, v in memo.items():
            # カードXを追加しない
            if k in newDP[card]:
                newDP[card][k] += v
            else:
                newDP[card][k] = v
            # カードXを追加するよ
            if k + x in newDP[card + 1]:
                newDP[card + 1][k + x] += v
            else:
                newDP[card + 1][k + x] = v
    dp = newDP

ans = 0
for i in range(1, N + 1):
    if A * i in dp[i]:
        ans += dp[i][A * i]
print(ans)
