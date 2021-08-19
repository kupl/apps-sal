def main():
    (n, a, b) = list(map(int, input().split()))
    x_list = list(map(int, input().split()))
    res = list()
    for x in x_list:
        res.append(str(x * a % b // a))
    print(' '.join(res))


def __starting_point():
    main()


__starting_point()
