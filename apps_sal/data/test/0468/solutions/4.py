from math import log
(x, y) = list(map(int, input().split()))
if x == y:
    print('=')
elif y * log(x) > x * log(y) + 1e-09:
    print('>')
elif y * log(x) + 1e-09 < x * log(y):
    print('<')
else:
    print('=')
