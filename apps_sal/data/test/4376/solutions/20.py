import bisect


def read_nums():
    return [int(x) for x in input().split()]


def main():
    n, m = read_nums()
    num_rums = read_nums()

    s = 0
    run_sums = [0]
    for run_num in num_rums:
        s += run_num
        run_sums.append(s)

    letters = read_nums()
    res = []
    for letter in letters:
        index = bisect.bisect_left(run_sums, letter)
        res.append((index, letter - run_sums[index - 1]))

    for r in res:
        print(r[0], r[1])


def __starting_point():
    main()


__starting_point()
