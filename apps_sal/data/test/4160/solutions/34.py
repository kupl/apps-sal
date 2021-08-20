import math
X = int(input())
money = 100
year = 0
while True:
    money = money + money // 100
    year += 1
    if money >= X:
        break
print(year)
