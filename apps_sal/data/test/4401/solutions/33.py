def main():
    x, y, z = list(map(int, input().split()))
    x, y = y, x
    x, z = z, x
    return '{} {} {}'.format(x, y, z)


def __starting_point():
    print((main()))


__starting_point()
