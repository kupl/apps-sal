
def __starting_point():
    x, y, z = list(map(int, input().split()))
    if x > y:
        up = x - y
        if z < up:
            print('+')
        else:
            print('?')
    elif y > x:
        down = y - x
        if z < down:
            print('-')
        else:
            print('?')
    else:
        if z == 0:
            print('0')
        else:
            print('?')


__starting_point()
