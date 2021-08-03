def read_nums():
    return [int(x) for x in input().split()]


def main():
    n, v = read_nums()
    res = 0
    cur_tank = 0
    for c in range(1, n + 1):
        need_to_by = min(v - cur_tank, n - c - cur_tank)
        res += need_to_by * c
        cur_tank += need_to_by
        cur_tank -= 1
    print(res)


def __starting_point():
    main()


__starting_point()
