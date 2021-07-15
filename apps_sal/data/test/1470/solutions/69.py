import math
x = int(input())
if x % 11 == 0:
    ans = x//11*2
else:
    ans = x//11*2
    y = x % 11
    if y <= 6:
        ans += 1
    else:
        ans += 2
print(ans)

