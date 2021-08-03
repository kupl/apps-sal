import math
X = int(input())

money, cnt = 100, 0
while money < X:
    money += money // 100
    cnt += 1
print(cnt)
