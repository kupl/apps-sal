h, w, k = map(int, input().split())
dp = [0] * (w)
l = [1, 1, 2, 3, 5, 8, 13, 21, 34]  # n本の縦線に高さ1のvalidな横棒を引く通り、フィボナッチ数列になる
# a_n:=n本の縦線にvalidな横棒を引く通りの総数、とすれば
# n+1本の時は1.1と2本目に横棒を引く（2と3の間に引けないのでa_n-1通り）
#          2.                引かない（a_n通り）
# よって漸化式a_n+1=a_n+a_n-1が成立。
dp[0] = 1
mod = 10**9 + 7
r = [0] * w
for i in range(h):
    for i in range(w):
        r[i] = dp[i] * l[i] * l[w - 1 - i]  # 左右に横棒を引かない
        if i >= 1:
            r[i] += dp[i - 1] * l[i - 1] * l[w - 1 - i]  # 左にのみ横棒を引く
        if i <= w - 2:
            r[i] += dp[i + 1] * l[i] * l[w - 2 - i]  # 右にのみ横棒を引く
        r[i] %= mod
    dp, r = r, dp

print(dp[k - 1])
