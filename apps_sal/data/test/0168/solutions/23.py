def read_nums():
    return [int(x) for x in input().split()]


def main():
    n, = read_nums()
    s = input()
    count = 0
    for ch in s:
        if ch == '+':
            count += 1
        else:
            count = max(count - 1, 0)
    print(count)


def __starting_point():
    main()

__starting_point()
