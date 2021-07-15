import sys

a,b,x,y = map(int, input().split())

diff = a - b
if diff == 1 or diff == 0:
    print(x)
    return

if diff < 0:
    diff = -diff
    p1 = x + y * diff
    p2 = (2 * diff * x) + x
else:
    p1 = x + y * (diff - 1)
    p2 = (diff * x) + x * (diff - 1)

print(min(p1, p2))
