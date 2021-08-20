def main():
    n = int(input())
    for i in range(2, n):
        if n % i == 0:
            print(str(i) + str(n // i))
            return


def __starting_point():
    main()


__starting_point()
