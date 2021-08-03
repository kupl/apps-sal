def main():
    input()
    l, a = [0, 0], '*'
    for b in input():
        l[a == b] += 1
        a = b
    print(l[0] + min(l[1], 2))


def __starting_point():
    main()


__starting_point()
