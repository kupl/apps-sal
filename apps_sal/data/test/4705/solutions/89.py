# 055A

# 1.入力をちゃんと受け取ること
x = input()
syoku = int(x)

# 2.結果を出力する
gokei = syoku * 800

if syoku // 15 != 0:
    print(gokei - 200 * (syoku // 15))
else:
    print(gokei)
