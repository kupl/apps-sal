def solve(n, a):
    lis = [0] * n
    for i in range(0, n):
        for j in range(0, i):
            if a[i] >= a[j]:
                lis[i] = max(lis[i], lis[j] + 1)
        if lis[i] == 0:
            lis[i] = 1
    print(n - max(lis))


def main():
    inp = lambda: int(input().split()[0])
    n = inp()
    a = [inp() for _ in range(n)]
    solve(n, a)


def __starting_point():
    main()


__starting_point()
