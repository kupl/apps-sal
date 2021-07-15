import math
h = int(input())
hp = h
c = 0
ans = 0

while hp > 1:
    hp = math.floor(hp/2)
    c += 1
for i in range(0,c+1):
    ans += 2 ** i
print(ans)
