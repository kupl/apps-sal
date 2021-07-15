def main():
    s = input()
    n = len(s)
    g = s.count('g')
    p = n - g
    ans = n // 2 - p
    print(ans)


def __starting_point():
    main()

__starting_point()
