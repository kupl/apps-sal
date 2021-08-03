x = int(input())
money = 100
cnt = 0
while money < x:
    money += money // 100
    cnt += 1
print(cnt)
