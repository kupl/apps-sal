def resolve():
    (a, b, c) = input().split()
    print('YES' if a[-1] == b[0] and b[-1] == c[0] else 'NO')


def __starting_point():
    resolve()


__starting_point()
