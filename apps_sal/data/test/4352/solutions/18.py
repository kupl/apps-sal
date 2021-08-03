a, b = map(int, input().split())
if a == 1 and b != 1:
    a += 13
    if a > b:
        print('Alice')
    elif b > a:
        print('Bob')
    else:
        print('Draw')
elif b == 1 and a != 1:
    b += 13
    if a > b:
        print('Alice')
    elif b > a:
        print('Bob')
    else:
        print('Draw')
elif a == 1 and b == 1:
    print('Draw')
else:
    if a > b:
        print('Alice')
    elif b > a:
        print('Bob')
    else:
        print('Draw')
