def main():
    n = int(input())
    s = input()
    l, r, c = 0, 0, 0
    for a in s:
        if a == '(':
            c += 1
        elif c:
            c -= 1
        else:
            l += 1
    r = c
    print(("(" * l + s + ")" * r))


def __starting_point():
    main()


__starting_point()
