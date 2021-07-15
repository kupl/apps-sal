X = int(input())
money = 100
years = 0

while money < X:
    money += money // 100
    years += 1
print(years)
