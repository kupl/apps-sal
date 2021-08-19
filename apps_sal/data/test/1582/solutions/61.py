def main():
    N = int(input())
    comb_count = [[0 for i in range(10)] for j in range(10)]
    res = 0
    for i in range(1, N + 1):
        s = str(i)
        (max, min) = (int(s[0]), int(s[-1]))
        comb_count[max][min] += 1
    for l in range(1, 10):
        for r in range(1, 10):
            res += comb_count[l][r] * comb_count[r][l]
    print(res)


def __starting_point():
    main()


__starting_point()
