def main():
    n = int(input())
    s = []
    if n == 0:
        print((0))
        return
    while n != 1:
        if n % (-2) == -1:
            n = n // (-2) + 1
            s.append(1)
        else:
            s.append(0)
            n = n // (-2)
    s.append(n)
    s.reverse()
    print((''.join([str(x) for x in s])))


def __starting_point():
    main()


__starting_point()
