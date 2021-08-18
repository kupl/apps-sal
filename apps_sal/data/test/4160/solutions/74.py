x = int(input())

year = 0
money = 100

while money < x:
    money = money * 101 // 100
    year += 1

print(year)
