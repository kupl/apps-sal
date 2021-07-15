x, y, z = map(int, input().split())
if x + z < y:
    print('-')
elif y + z < x:
    print('+')
elif y == x and z == 0:
    print('0')
else:
    print('?')
