from math import log
x, y = list(map(int, input().split()))
if x == 1:
    if y == 1:
        print('=')
    else:
        print('<')
else:
    if y == x * log(y, x):
        print('=')
    elif y < x * log(y, x):
        print('<')
    else:
        print('>')
