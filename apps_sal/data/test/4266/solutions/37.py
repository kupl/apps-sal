
def main():
    k, x = list(map(int, input().split()))
    ans = list(range(x - k + 1, x + k))
    print((*ans))


def __starting_point():
    main()


__starting_point()
