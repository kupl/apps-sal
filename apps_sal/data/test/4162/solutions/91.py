def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) - n)


def __starting_point():
    main()


__starting_point()
