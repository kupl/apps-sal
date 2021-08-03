import statistics


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    c = [a[i] - i - 1 for i in range(n)]
    b = int(statistics.median(c))
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b + i + 1))
    print(ans)


def __starting_point():
    main()


__starting_point()
