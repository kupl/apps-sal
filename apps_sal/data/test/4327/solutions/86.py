url = 'https://atcoder.jp//contests/abc128/tasks/abc128_a'


def main():
    (a, p) = list(map(int, input().split()))
    p += a * 3
    print(p // 2)


def __starting_point():
    main()


__starting_point()
