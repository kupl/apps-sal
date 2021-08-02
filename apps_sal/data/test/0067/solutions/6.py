x, y, z = list(map(int, input().split()))
a = x - y
if abs(a) - z > 0:
    if a < 0:
        print('-')
    elif a == 0:
        print(0)
    else:
        print('+')
elif a == 0 and z == 0:
    print(0)
else:
    print('?')
