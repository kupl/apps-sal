
h, w = list(map(int, input().split()))
a = []
for i in range(h):
    ai = list(map(int, input().split()))
    a.append(ai)
for i in range(h):
    bi = list(map(int, input().split()))
    for j in range(w):
        a[i][j] -= bi[j]
        a[i][j] = abs(a[i][j])
# 差のmaxまでをlistで確保する代わりに可能な値をsetで保持
# 値が小さいのでsetからbitで保持に変更
dp = [[0 for j in range(w)] for i in range(h)]
a2 = [a[i][j] for i in range(h) for j in range(w)]
mxa = max(a2)
# 中心を取る
# 間違えやすいし最大値決め打ちか
tmp = 1 << mxa * (h + w) + 10

dp[0][0] |= tmp << a[0][0]
dp[0][0] |= tmp >> a[0][0]

for j in range(1, w):
    dp[0][j] = dp[0][j - 1] << a[0][j]
    dp[0][j] |= dp[0][j - 1] >> a[0][j]

for i in range(1, h):
    for j in range(w):  # ループ一つ抜けてるわw
        dp[i][j] = dp[i - 1][j] << a[i][j]
        dp[i][j] |= dp[i - 1][j] >> a[i][j]
        if j:
            dp[i][j] |= dp[i][j - 1] << a[i][j]
            dp[i][j] |= dp[i][j - 1] >> a[i][j]

tmp1 = dp[h - 1][w - 1]

tmp1 >>= mxa * (h + w) + 10

# mxa=0でrange(0)になる式だと答えが出ない
for k in range(mxa * (h + w) + 10):
    if tmp1 & 1:
        print(k)
        return
    tmp1 >>= 1
