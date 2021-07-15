x, y = map(int, input().split())
b = (y/2 - x)
a = x - b
if y % 2 != 0:
    print('No')
elif b < 0:
    print('No')
elif a >= 0:
    print('Yes')
else:
    print('No')
