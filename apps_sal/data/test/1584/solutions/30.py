import bisect


def main():
    n = int(input())
    l = sorted(list((int(i) for i in input().split())))
    cnt = 0
    for i in range(n - 2):
        a = l[i]
        for j in range(i + 1, n - 1):
            b = l[j]
            cnt += bisect.bisect_left(l, a + b) - (j + 1)
    print(cnt)


def __starting_point():
    main()


__starting_point()
