import math
x, y = map(int, input().split())
if math.log10(x) * y > math.log10(y) * x:
    print('>')
elif math.log10(x) * y < math.log10(y) * x:
    print('<')
else:
    print('=')
