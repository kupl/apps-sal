def read_nums():
    return [int(x) for x in input().split()]


def main():
    (n,) = read_nums()
    cur_res = 1
    factorial = 1
    for i in range(2, n + 1):
        factorial = factorial * i % 998244353
        cur_res = ((cur_res - 1) * i + factorial) % 998244353
    print(cur_res)


def __starting_point():
    main()


__starting_point()
