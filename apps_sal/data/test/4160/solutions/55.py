import math
x = int(input())
now = 100
ans = 0
while(now < x):
    ans += 1
    now += now // 100
print(ans)
