def main():
    l, r = (format(int(s), 'b') for s in input().split())
    le = len(r)
    if len(l) == le:
        for i in range(le):
            if l[i] != r[i]:
                print(int('1' * (le - i), 2))
                break
        else:
            print(0)
    else:
        print(int('1' * le, 2))


def __starting_point():
    main()

__starting_point()
