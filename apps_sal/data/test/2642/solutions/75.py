from math import gcd
mod = 1000000007
n = int(input())
zero = 0
bad = {}  # 仲が悪い者同士をグループ化
for i in range(n):
    x, y = list(map(int, input().split()))
    if x == 0 and y == 0:
        zero += 1  # (A,B) = (0,0) の計数をとる
        continue
    g = gcd(x, y)
    x //= g  # ベクトルを整数の範囲で最小化し、
    y //= g  # 傾きを既約分数 (y'/x') の形にする
    # ベクトルを0≦θ＜πの範囲に変換する
    if y < 0: x, y = -x, -y  # 第3~4象限のベクトルはπ回転
    if y == 0 and x < 0: x, y = -x, -y  # θ=πのベクトルはθ=0へ
    # π/2≦θ＜πは、π/2回転して同じキーにする
    is_rotate90 = (x <= 0)
    if is_rotate90: x, y = y, -x  # π/2回転
    if not (x, y) in bad: bad[x, y] = [0, 0]
    # π/2回転したもの、してないものは別に計数をとる
    bad[x, y][is_rotate90] += 1

ans = 1  # 組み合わせを掛けていくので 1 から
for x, y in bad:
    c1, c2 = bad[x, y]
    # c1, c2 両方選択は仲が悪いのでできない
    # c1 の側のみを 1 個以上選択する
    # c2 の側のみを 1 個以上選択する
    # c1, c2 どちらも選択しない
    c3 = (pow(2, c1, mod) - 1) + (pow(2, c2, mod) - 1) + 1
    ans *= c3
    ans %= mod

# (A,B)=(0,0)は、単独でしか選択できないので、+zero する
# 全て未選択はできないので、-1 する
ans += zero - 1
ans = (ans + mod) % mod  # 負数対応
print(ans)
