def solve(n, p):
    cnt = 2 * n + p
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            print(i, j)
            cnt -= 1
            if cnt == 0:
                return


def main():
    t = int(input())
    for _ in range(t):
        (n, p) = map(int, input().split())
        solve(n, p)


def __starting_point():
    main()


__starting_point()
