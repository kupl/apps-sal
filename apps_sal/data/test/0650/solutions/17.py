def main():
    a = set('AEFHIKLMNTVWXYZ')
    b = set('BCDGJOPQRSU')
    w = list(input())
    in_a = False
    in_b = False
    for l in w:
        in_a = in_a or l in a
        in_b = in_b or l in b

    if in_a and in_b:
        print('NO')
    else:
        print('YES')


def __starting_point():
    main()

__starting_point()
