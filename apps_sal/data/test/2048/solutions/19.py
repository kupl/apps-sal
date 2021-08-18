def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    Max = 2 * sum(c)

    f = [x for x in c]
    for _ in range(2):
        for i in range(n - 1, -1, -1):
            min_fj = Max
            for j in range(i):
                if s[j] < s[i]:
                    min_fj = min(f[j], min_fj)
            if min_fj == Max:
                f[i] = Max
            else:
                f[i] = min_fj + c[i]

    min_cost = min(f)
    if min_cost == Max:
        print(-1)
    else:
        print(min_cost)


def __starting_point():
    main()


__starting_point()
