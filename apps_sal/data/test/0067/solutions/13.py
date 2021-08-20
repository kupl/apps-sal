(x, y, z) = map(int, input().split())
if x + z < y:
    print('-')
elif x > y + z:
    print('+')
elif z == 0:
    print('0')
else:
    print('?')
