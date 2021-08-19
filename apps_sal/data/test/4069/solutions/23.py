from bisect import bisect_left, bisect_right


def main():
    s = [int(x) for x in input().split()]
    (x, k, d) = (s[0], s[1], s[2])
    tmp = abs(x) // d
    if tmp >= k:
        mini = abs(x) - d * k
    else:
        mini = abs(abs(x) - tmp * d)
        if (k - tmp) % 2 == 1:
            mini = abs(mini - d)
    print(mini)


def __starting_point():
    main()


__starting_point()
