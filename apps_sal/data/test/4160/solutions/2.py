x = int(input())
money = 100
years = 0

while money < x:
    money += money // 100
    years += 1

print(years)
