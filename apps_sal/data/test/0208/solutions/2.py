import math
x1, y1, x2, y2 = map(int,input().split())
a = abs(x1-x2)
b = abs(y1-y2)
if a == b and a != 0:
    print(x1, y2, x2, y1)
elif a == 0 and b != 0:
    print(x1 + b, y1, x1+b, y2)
elif b == 0 and a != 0:
    print(x1, y1 + a, x2, y1 + a)
else:
    print(-1)
