x,y,z = map(int, input().split())
a = x - y
if a + z < 0:
    print('-')
elif a - z > 0:
    print('+')
elif a + z == a - z and a + z == 0:
    print(0)
else:
    print('?')
