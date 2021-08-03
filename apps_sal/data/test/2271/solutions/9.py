def main():
    n = int(input())
    l = [-1] * (n + 1)
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        l[a] += 1
        l[b] += 1
    res = 0
    for x in [_f for _f in l if _f]:
        res += x * (x + 1)
    print(res // 2)


def __starting_point():
    main()


__starting_point()
