X = int(input())
money = 100
year = 0
while money < X:
    money = money + money//100
    year += 1
print(year)
