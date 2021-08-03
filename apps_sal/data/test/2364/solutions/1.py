MOD = 998244353


def main():
    n = int(input())
    a = [int(x) for x in input().split(' ')]

    p, sp, s, ss = 0, 0, 0, 0
    for x in a:
        ss = (2 * ss + s) % MOD
        s = (s + x) % MOD
        p = (ss + sp + s) % MOD
        sp = (sp + p) % MOD
    print(p)


def __starting_point():
    main()


__starting_point()
