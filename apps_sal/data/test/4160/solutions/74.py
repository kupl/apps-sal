x = int(input())

year = 0  # 答え
money = 100  # 初期値の100円

# x円以上になるまでループを回す
while money < x:
    money = money * 101 // 100
    year += 1

print(year)
