"""

https://atcoder.jp/contests/arc109/tasks/arc109_e

同色連続をブロックとして考える
3ブロック以上になることはない
[証明]
2ブロック以下とする。
同色側に置くと何も変わらない。異色側に置くと2ブロックになるか、1ブロックになる

端が同じ色なら、全てその色になる→よって期待値は半分

端が違う色の時を考える
WWB?????S?????WBBB
端の自分の色のブロックに先に到達した方が端以外を総取りできる

距離が同じときのみ黒が勝てる
→これだけ考えればよい

sの位置が決まる
sから端ブロックまでの距離がxの時の通り数は

WWB????S????WBBBB

2*pow(2,2x-3)
である

取れるBの個数は、両側を同時に加味すると
n+2x-1

よって (n+2x-1)*pow(2,2x-3)
を計算していけばよい

"""


def inverse(a, mod):
    return pow(a, mod - 2, mod)


mod = 998244353
half = 499122177
n = int(input())
inv = inverse(pow(2, n, mod), mod)
cnum = 0
black = 0
ans = [0] * n
for s in range(n):
    if s * 2 < n:
        if s >= 2:
            cnum += 2 * pow(2, 2 * s - 3, mod)
            black += (n + 2 * s - 1) * pow(2, 2 * s - 3, mod)
        ans[s] = ((pow(2, n, mod) - cnum) * n * half + black) * inv % mod
        print(ans[s])
    else:
        print(ans[n - 1 - s])
