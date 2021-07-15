X = int(input())

money = 100
year = 0

while True:
    if money >= X:
        break
    money += money//100
    year += 1

print(year)
