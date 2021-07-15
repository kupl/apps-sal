def main():
    input()
    a1 = a2 = x1 = x2 = z = 0
    for b in map(int, input()[::2]):
        if 0 < b < 3:
            if a1 == b:
                a1 = 0
                x1 += 1
            else:
                a1 = b
            if a2 == b:
                a2 = 0
                x2 += 1
            else:
                a2 = b
            if x1 != x2:
                if x1 > x2:
                    x1, a1 = x2, a2
                else:
                    x2, a2 = x1, a1
        elif b:  # 3
            a1 = 1 if a1 != 1 else 2
            a2 = 2 if a2 != 2 else 1
        else:  # 0
            a1 = a2 = 0
            z += 1
    print(x1 + z)


def __starting_point():
    main()

__starting_point()
