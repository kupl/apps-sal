def LI():
    return list(map(int, input().split()))


def I():
    return map(int, input().split())


mod = 10 ** 9 + 7


def main():
    (n, d) = map(int, input().split())
    x = [LI() for i in range(n)]
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            sm = 0
            for k in range(d):
                sm += (x[i][k] - x[j][k]) ** 2
            if sm ** 0.5 % 1 == 0:
                ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
