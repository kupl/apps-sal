def main():
    n = int(input())
    ans = 0
    for a in range(1, 10 ** 6 + 1):
        b = 1
        while a * b < n:
            ans += 1
            b += 1
    print(ans)


def __starting_point():
    main()

__starting_point()
