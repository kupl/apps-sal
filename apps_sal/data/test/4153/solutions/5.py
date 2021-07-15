def main2():
    s = input()
    one = s.count('0')
    zero = s.count('1')
    print(min(one, zero)*2)


def __starting_point():
    main2()
__starting_point()
