K = int(input())
S = input()
N = len(S)
mod = int(1e9 + 7)

# 123
# a1bb2ccc3dddd 10文字インサート
# pow(25,6) * pow(26,4) * 8C2
# (3はfixで、それより前の8mojiから1/2を入れる場所を決める）
# これを3の位置でループする（1-indexで 3<=i<=N)

# 123dddddddddd
# pow(25,0) * pow(26,10) * 2C2(1)
# 12x3ddddddddd
# pow(25,1) * pow(26,9) * 3C2( = 2C2 * 3 / 1)
# 12xx3dddddddd
# pow(25,2) * pow(26,8) * 4C2( = 3C2 * 4 / 2)
# ...
# 12xxxxxxxxxx3
# pow(25,10) * pow(26,0) * 12C2( = 11C2 * 12 / 10)

# 5C5, 6C5, 7C5 1, 6, 21, 56

wk = pow(26, K, mod)
inv26 = pow(26, -1, mod)

ans = wk
for i in range(1, K + 1):
    wk = (wk * 25 * inv26) % mod
    wk = (wk * (N - 1 + i) * pow(i, -1, mod) % mod)
    ans = (ans + wk) % mod

print(ans)
