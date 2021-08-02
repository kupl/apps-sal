def main():
    K = int(input())

    ans = -1
    r = 7 % K
    for i in range(1, K + 1):
        if r == 0:
            ans = i
            break
        r = (10 * r + 7) % K
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
