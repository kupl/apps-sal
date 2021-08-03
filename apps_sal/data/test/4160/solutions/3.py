import math

x = int(input())
money = 100
year = 0
while money < x:
    money += money // 100
    year += 1
print(year)
