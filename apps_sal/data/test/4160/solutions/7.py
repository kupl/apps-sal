x = int(input())
money = 100
cnt = 0

while x > money:
    money += money // 100
    cnt += 1
print(cnt)
