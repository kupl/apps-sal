def __starting_point():
    (y, x) = [int(i) for i in input().strip().split()]
    if y == x - 1:
        print('Yes')
    elif y < x - 1:
        print('No')
    else:
        valid = abs(y - (x - 1)) % 2 == 0 and x - 1 > 0
        print('Yes' if valid else 'No')


__starting_point()
