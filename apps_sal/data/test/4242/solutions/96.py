a,b,k = map(int,input().split())
# aの約数
a_divisor = []
# abの公約数
ab_divisor = []

# aで割れたら順次約数に追加
for i in range(1,a+1):
    if a % i == 0:
        a_divisor.append(i)

# aの約数でbが割れたら公約数に追加
for j in a_divisor:
    if b % j == 0:
        ab_divisor.append(j)
# リストの大きい方からK番目の数値を出力
print(ab_divisor[-k])
