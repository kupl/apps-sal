def resolve():
    print(2 ** (len(bin(int(input()))) - 3))


def __starting_point():
    resolve()
__starting_point()
