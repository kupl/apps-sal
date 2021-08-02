def d(a, x):
    t = 0
    for n in a:
        t += abs(n - x)
    return t


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        if d(a, a[n // 2 - 1]) <= d(a, a[n // 2]):
            print(a[n // 2 - 1])
        else:
            print(a[n // 2])
    else:
        print(a[n // 2])


def main():
    solve()


def __starting_point():
    main()


__starting_point()
