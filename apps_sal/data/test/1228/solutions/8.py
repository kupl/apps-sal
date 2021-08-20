def __starting_point():
    n = int(input())
    rem = n % 4
    if rem == 1:
        print(0, 'A')
    if rem == 3:
        print(2, 'A')
    if rem == 2:
        print(1, 'B')
    if rem == 0:
        print(1, 'A')


__starting_point()
