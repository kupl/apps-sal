# 入力
# 値は全てint
# Nは本数、Kは切る回数、AはN本の木のそれぞれの長さ(リスト)
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 二分探索
# lが左端、rが右端
l, r = 0, 10**9

# 整数で返すので、差が１より大きい時はループする
while r - l > 1:
    # 真ん中を設定
    x = (r + l) // 2

    # 切る回数をc
    c = 0
    for a in A:
        # それぞれの丸太の(長さ-1)をxで割った値の合計が、切る回数
        c += (a - 1) // x

    # 切る回数がKよりも小さい時はOKなので右端を寄せる
    if c <= K:
        r = x
    else:
        l = x

print(r)
