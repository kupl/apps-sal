def main():
    S, P = list(map(int, input().split()))
    n = 1
    while n**2 <= P:
        m = S - n
        if P % n == 0 and P // n == m:
            print("Yes")
            return
        n += 1
    print("No")


def __starting_point():
    main()


__starting_point()
