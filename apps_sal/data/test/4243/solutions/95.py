def main():
    x = int(input())
    a = x // 500
    b = (x - 500 * a) // 5
    ans = int(a * 1000 + b * 5)
    print(ans)


def __starting_point():
    main()

__starting_point()
