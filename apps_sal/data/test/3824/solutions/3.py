import math
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if x1 == x2:
    ans = 2*abs(y1-y2)+6
elif y1 == y2:
    ans = 2*abs(x1-x2)+6
else:
    ans = 2 * (abs(x1 - x2) + 1 + abs(y1 - y2) + 1)
print(ans)
