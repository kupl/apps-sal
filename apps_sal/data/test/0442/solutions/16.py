def __starting_point():
    r = int(input())
    if r < 5:
        print('NO')
    elif r % 2 == 0:
        print('NO')
    else:
        y = (r - 3) // 2
        print('1 ' + str(y))


__starting_point()
