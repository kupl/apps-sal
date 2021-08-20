(x, y) = map(int, input().split())
if x == y:
    print('=')
elif x == 1:
    print('<')
elif y == 1:
    print('>')
elif x == 2 and y == 3:
    print('<')
elif x == 3 and y == 2:
    print('>')
elif x == 4 and y == 2:
    print('=')
elif x == 2 and y == 4:
    print('=')
elif x < y:
    print('>')
elif x > y:
    print('<')
