import math
def func(a, b):
    x = b*math.log2(a)
    y = a*math.log2(b)
    if x>y:
        return '>'
    elif y>x:
        return '<'
    else:
        return '='

s = input().split()
print(func(int(s[0]), int(s[1])))
