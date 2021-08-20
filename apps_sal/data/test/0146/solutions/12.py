def main():
    buf = input()
    buflist = buf.split()
    n = int(buflist[0])
    k = int(buflist[1])
    buf = input()
    buflist = buf.split()
    tab = list(map(int, buflist))
    test_count = 0
    social_count = 0
    for i in range(n):
        if tab[i] == 1:
            test_count += 1
        else:
            social_count += 1
    max_diff = 0
    for i in range(k):
        test_remaining = test_count
        social_remaining = social_count
        for j in range(i, n, k):
            if tab[j] == 1:
                test_remaining -= 1
            else:
                social_remaining -= 1
        diff = abs(test_remaining - social_remaining)
        if diff > max_diff:
            max_diff = diff
    print(max_diff)


def __starting_point():
    main()


__starting_point()
