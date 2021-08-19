from math import floor
X = int(input())
money = 100
year = 0
while money < X:
    year += 1
    money += money // 100
print(year)
