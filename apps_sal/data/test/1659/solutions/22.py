def main():
    n, cur = list(map(int, input().split()))
    frustr = 0
    for i in range(n):
        c, amo = input().split()
        amo = int(amo)
        if c == '+':
            cur += amo
        else:
            if cur >= amo:
                cur -= amo
            else:
                frustr += 1
    print(cur, frustr)


def __starting_point():
    main()


__starting_point()
