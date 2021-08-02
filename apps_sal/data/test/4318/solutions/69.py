def main():
    sea = 1
    n = int(input())
    h = list(map(int, input().split()))
    mountain = h[0]
    for i in range(1, n):
        if mountain <= h[i]:
            sea += 1
            mountain = h[i]
    print(sea)


def __starting_point():
    main()


__starting_point()
