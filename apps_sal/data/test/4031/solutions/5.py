def read_nums():
    return [int(x) for x in input().split()]


def is_good(strings):
    for i in range(1, len(strings)):
        if strings[i - 1] not in strings[i]:
            return False
    return True


def main():
    (n,) = read_nums()
    strings = []
    for _ in range(n):
        strings.append(input())
    strings = sorted(strings, key=lambda x: len(x))
    if is_good(strings):
        print('YES')
        for s in strings:
            print(s)
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
