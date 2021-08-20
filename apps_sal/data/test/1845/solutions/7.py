def read_nums():
    return [int(x) for x in input().split()]


def get_divisors(num):
    res = []
    for i in range(2, num + 1):
        if num % i == 0:
            res.append(i)
    return res


def solve(powers):
    s = sum(powers)
    smallest = min(powers)
    cur_res = s
    for num in set(powers):
        for divisor in get_divisors(num):
            candidate = s - num + num // divisor - smallest + smallest * divisor
            cur_res = min(cur_res, candidate)
    print(cur_res)


def main():
    (n,) = read_nums()
    powers = read_nums()
    solve(powers)


def __starting_point():
    main()


__starting_point()
