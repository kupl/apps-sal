# すめけくんは
# 現在のレートが 1200未満ならば AtCoder Beginner Contest (ABC) に、
# そうでなければ AtCoder Regular Contest (ARC) に参加することにしました。
# すめけくんの現在のレート xが与えられます。
# すめけくんが参加するコンテストが ABC ならば ABC と、そうでなければ ARC と出力してください。

# 制約
# 1 ≦ x ≦ 3,000
# x は整数

# 標準入力から x を取得する
x = int(input())

# レートを判定して結果を出力する
result = "ret"

if x < 1200:
    result = "ABC"
else:
    result = "ARC"

print(result)
