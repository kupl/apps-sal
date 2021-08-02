def main():
    n, k = list(map(int, input().split()))
    if k % 2 == 1:
        c = n // k
        print((c**3))
        return
    if k % 2 == 0:
        c = (n - k // 2) // k + 1
        ans = c**3
        c = n // k
        print((ans + c**3))


def __starting_point():
    main()


__starting_point()
