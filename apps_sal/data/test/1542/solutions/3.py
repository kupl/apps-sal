from bisect import bisect_right


def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    q = int(input())
    for i in range(q):
        m = int(input())
        res = bisect_right(x, m)
        print(res)


def __starting_point():
    main()


__starting_point()
