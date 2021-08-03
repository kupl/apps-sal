import math
x, y = list(map(int, input().split()))
if x == 1 or y == 1:
    if x**y == y**x:
        print('=')
    elif x**y > y**x:
        print('>')
    else:
        print('<')
    return
x, y = y, x * math.log(y, x)
if x == y:
    print('=')
elif x > y:
    print('>')
else:
    print('<')
