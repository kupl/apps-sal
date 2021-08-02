def main():
    n = int(input())
    m = n // 2 + 1
    print(m)
    for i in range(m):
        print(str(i + 1) + " 1")
    for i in range(m + 1, n + 1):
        print(str(m) + " " + str(i - m + 1))


def __starting_point():
    main()


__starting_point()
