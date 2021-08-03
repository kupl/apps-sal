def main():
    n = int(input())
    aa = list(map(int, input().split()))
    m = aa[-1]
    for i in range(n - 2, -2, -1):
        a = aa[i]
        if m < a:
            break
        m = a
    print(i + 1)


def __starting_point():
    main()


__starting_point()
