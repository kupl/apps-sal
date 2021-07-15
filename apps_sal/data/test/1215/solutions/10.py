def __starting_point():
    n = int(input())
    if n % 2 == 1:
        print(0)
    else:
        print(2 ** (n // 2))
__starting_point()
