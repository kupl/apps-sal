def main():
    n, m = list(map(int, input().split()))
    if n == 1:
        print(1)
    else:
        left, right = max(0, m - 1), max(0, n - m)
        if left >= right:
            print(m - 1)
        else:
            print(m + 1)


def __starting_point():
    main()

__starting_point()
