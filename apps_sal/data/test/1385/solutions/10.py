def main():
    res = []
    for i, s in enumerate(input().split('"')):
        if i & 1:
            res += ["<", s, ">\n"]
        else:
            for t in s.split():
                res += ["<", t, ">\n"]
    print(''.join(res), end='')


def __starting_point():
    main()


__starting_point()
