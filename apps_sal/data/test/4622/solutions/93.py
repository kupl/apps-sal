def main():
    N = int(input())
    print('YES' if len(set(input().split())) == N else 'NO')


def __starting_point():
    main()


__starting_point()
