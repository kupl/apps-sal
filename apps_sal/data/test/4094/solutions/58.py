def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    r = 7 % K
    n = 1
    while r != 0:
        r = (10 * r + 7) % K
        n += 1
    print(n)
    return


def __starting_point():
    main()


__starting_point()
