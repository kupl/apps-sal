import bisect


def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    if len(a) < 3:
        print(a[1], a[0])
        return
    N = a[-1]
    a = a[:-1]
    r = bisect.bisect(a, N / 2)
    if r == 0:
        R = a[0]
    if r == len(a):
        R = a[r - 1]
    else:
        R = a[r] if abs(a[r - 1] - N / 2) > abs(a[r] - N / 2) else a[r - 1]
    print(N, R)


def __starting_point():
    main()


__starting_point()
