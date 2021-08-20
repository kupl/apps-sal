(x, y, z) = list(map(int, input().split()))
if x + z < y:
    print('-')
elif y + z < x:
    print('+')
elif z == 0 and x == y:
    print(0)
else:
    print('?')
