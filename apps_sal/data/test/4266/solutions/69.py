url = 'https://atcoder.jp//contests/abc137/tasks/abc137_b'


def main():
    (k, x) = list(map(int, input().split()))
    for i in range(x - k + 1, k + x):
        print(i, end=' ')
    print()


def __starting_point():
    main()


__starting_point()
