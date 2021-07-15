from decimal import Decimal
X = int(input())
n = 0
money = 100
while True:
    money += int(money * Decimal("0.01"))
    #print(money)
    n += 1
    if money >= X:
        print(n)
        break
