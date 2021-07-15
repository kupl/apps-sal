x = int(input())
money = 100
count = 1
while True:
    money += money // 100
    if money >= x:
        break
    count += 1
print(count)

