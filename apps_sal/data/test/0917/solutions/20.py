def main():
    (n, h, m) = list(map(int, input().split()))
    restrictions = [h for _ in range(n)]
    for i in range(m):
        (l, r, x) = list(map(int, input().split()))
        for j in range(l, r + 1):
            restrictions[j - 1] = min(restrictions[j - 1], x)
    res = 0
    for x in range(n):
        res += restrictions[x] ** 2
    print(res)


def __starting_point():
    main()


__starting_point()
