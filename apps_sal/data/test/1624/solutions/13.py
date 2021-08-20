def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ret = 0
    for i in range(n // 2):
        ret += (a[i] + a[n - i - 1]) ** 2
    print(ret)


def __starting_point():
    main()


__starting_point()
