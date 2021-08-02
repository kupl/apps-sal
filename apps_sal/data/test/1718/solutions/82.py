def main():
    n, k = map(int, input().split())
    ans = 0 if (n - 1) % (k - 1) == 0 else 1
    ans += (n - 1) // (k - 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
