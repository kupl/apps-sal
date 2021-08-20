import math
x = int(input())
money = 100
ans = 0
while money < x:
    money += money // 100
    ans += 1
print(ans)
