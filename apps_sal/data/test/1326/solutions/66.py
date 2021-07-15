def main():
    n = int(input())
    ans = 0
    x = n // 2
    for i in range(1, n + 1):
        m = n // i
        ans += i * ((m + 1) * m) // 2
    print(ans)


def __starting_point():
    main()

__starting_point()
