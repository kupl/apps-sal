def get_ints(string):
    return list(map(int, string.split()))


def get_input():
    n = int(input())
    xs = get_ints(input())
    return n, xs


def foo(xs, res, last):
    # print(xs)
    if len(xs) is []:
        return res
    for i, x in enumerate(xs):
        if x == 0:
            res += 1
            last = 0

        elif x == 1 and last == 1:
            res += 1
            last = 0
        elif x == 1:
            last = 1

        elif x == 2 and last == 2:
            res += 1
            last = 0
        elif x == 2:
            last = 2

        else:
            if last == 1:
                last = 2
            elif last == 2:
                last = 1
            elif i < len(xs) - 1 and xs[i + 1] == 0:
                last = 1
            else:
                return min(foo(xs[i + 1:], res, 1), foo(xs[i + 1:], res, 2))

    return res


def main():
    n, xs = get_input()
    res = foo(xs, 0, 0)

    print(res)
    return res


def __starting_point():
    main()


__starting_point()
