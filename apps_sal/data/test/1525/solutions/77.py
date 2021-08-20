"""Yoshichiの日記
あみだくじ。
0本目からスタートし、W本の長さH + 1までにを任意の線を引いた時
K本目にたどり着くパターンは何パターンあるか答えよ。
現在の位置状態での線の引き方を全列挙し、DP(メモ化再帰)を用いて答える。
x → 現在の位置
y → 現在の進み具合
for分のi → 現在の位置にいる時の線の配置状態(1が隣接へつながっているとき)
for分のj → NGパターンの列挙(隣へ繋がっているかつ、
                   次の隣へも線が引かれている状態)
"""
from collections import defaultdict
(h, w, k) = map(int, input().split())
memo = defaultdict(lambda: defaultdict(int))


def dfs(x, y):
    if y == h:
        if x == k - 1:
            return 1
        else:
            return 0
    if y in memo[x]:
        return memo[x][y]
    ans = 0
    for i in range(1 << w - 1):
        flg = True
        for j in range(w - 2):
            if i & 1 << j and i & 1 << j + 1:
                flg = False
                break
        if flg:
            nx = x
            if x > 0 and i & 1 << x - 1:
                nx = x - 1
            elif i & 1 << x:
                nx = x + 1
            ans += dfs(nx, y + 1)
            ans %= 1000000000 + 7
    memo[x][y] = ans
    return ans


print(dfs(0, 0))
