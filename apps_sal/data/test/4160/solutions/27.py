x = int(input())
# 基礎のデータの設定をする
# 残高y100円　年数nを0とする
y = 100
n = 0
# 毎年金利1％だから繰り返し
while y < x:
    n += 1
    y += y // 100
print(n)
