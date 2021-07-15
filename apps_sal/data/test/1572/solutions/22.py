def main():
    n = int(input())
    l = list(map(int, input().split()))
    res = len(l)
    if res > 2:
        res = m = 2
        for i in range(2, n):
            if l[i] == l[i - 1] + l[i - 2]:
                m += 1
            else:
                if res < m:
                    res = m
                m = 2
        if res < m:
            res = m
    print(res)


def __starting_point():
    main()
__starting_point()
