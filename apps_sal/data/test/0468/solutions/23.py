import math
(x, y) = list(map(int, input().split()))
if x == 2 and y == 4:
    print('=')
elif y == 2 and x == 4:
    print('=')
elif x == y:
    print('=')
elif y * math.log(x) < x * math.log(y):
    print('<')
else:
    print('>')
