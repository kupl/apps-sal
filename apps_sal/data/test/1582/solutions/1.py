def main():
    import sys
    from collections import defaultdict

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    nd = defaultdict(int)
    for i in range(1, n + 1):
        tmp = str(i)
        h, t = int(tmp[0]), int(tmp[-1])
        nd[(h, t)] += 1

    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ans += nd[(i, j)] * nd[(j, i)]
    print(ans)


def __starting_point():
    main()


__starting_point()
