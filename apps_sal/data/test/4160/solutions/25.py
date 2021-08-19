X = int(input())
money = 100
y = 0
while True:
    money = 101 * money // 100
    y += 1
    if money >= X:
        print(y)
        break
