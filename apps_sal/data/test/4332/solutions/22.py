def main():
    n = input()
    s = 0
    for i in n:
        s += int(i)
    if int(n) % s == 0:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
