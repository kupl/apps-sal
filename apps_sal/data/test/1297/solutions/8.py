def main():
    (a, cnt, res) = ('*', 1, 0)
    for b in input() + '*':
        if a != b:
            res += 1 - (cnt & 1)
            cnt = 1
            a = b
        else:
            cnt += 1
    print(res)


def __starting_point():
    main()


__starting_point()
