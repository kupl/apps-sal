def read_nums():
    return [int(x) for x in input().split()]


def main():
    n, = read_nums()
    cipher = input()
    i = 0
    d = 1
    res = ''
    while i < n:
        res += cipher[i]
        i += d
        d += 1
    print(res)


def __starting_point():
    main()

__starting_point()
