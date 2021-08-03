happy = 0

money = int(input())

coin, money = divmod(money, 500)

happy += 1000 * coin

coin, money = divmod(money, 5)

happy += 5 * coin

print(happy)
