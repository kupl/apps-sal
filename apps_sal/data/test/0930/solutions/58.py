# 0人になる部屋の数
# ・最小0 (k = 1　ないしは　N = 2 and k = 3が制約外なので必ず0になる)
# ・最大 min(k,N-1) (k人が部屋を空に出来るが、1部屋は必ず空でない部屋が残る)
# min(k,N-1)部屋が空になるということは、N-min(k,N-1)部屋には必ず人がいる
# 空でない部屋の最大数はN - K
# N - K - 1部屋に割り振るパターンはあり得ない
# つまりN-min(k,N-1)-1部屋に人がいるケースはあり得ない
# N人をN部屋に割り振る場合の数から、
# N人をN-min(k,N-1)-1部屋に割り振る場合の数を引く
# いずれも0の場合を含む
# N個をK箱に割り振る場合の数は、N+K-1 C N

DIV = 10 ** 9 + 7
n = 10**6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, n + 1):
    g1.append((g1[-1] * i) % DIV)
    inverse.append((-inverse[DIV % i] * (DIV // i)) % DIV)
    g2.append((g2[-1] * inverse[-1]) % DIV)


def nCr(n, r, DIV):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % DIV


N, K = map(int, input().split())

# N人をN部屋に割り振る場合の数から、
# N人をN-min(k,N-1)-1部屋に割り振る場合の数を引く
# いずれも0の場合を含む
# N個をK箱に割り振る場合の数は、N+K-1 C N

ans = 0
for i in range(min(K, N - 1) + 1):
    a = nCr(N, i, DIV)

    # N-i個の部屋にN個のボールを詰める
    # N個のうちのN-i個をまず1個ずつ詰める
    # 残りはN - (N - i) = i個
    # i個のボールをN-i個に詰める。i個と(N-i-1)個の仕切りの並び替え
    # (i + N - i - 1) C i = (N-1) C i
    b = nCr(N - 1, i, DIV)

    ans += (a * b) % DIV
    ans %= DIV

print(ans)
