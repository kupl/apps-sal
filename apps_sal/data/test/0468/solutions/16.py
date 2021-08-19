(x, y) = map(int, input().split())
if x == 1 and y == 1:
    print('=')
elif x == 1 and y > 1:
    print('<')
elif x > 1 and y == 1:
    print('>')
elif x <= 100 and y <= 100:
    if x ** y > y ** x:
        print('>')
    elif x ** y < y ** x:
        print('<')
    else:
        print('=')
elif x > y:
    print('<')
elif x < y:
    print('>')
else:
    print('=')
