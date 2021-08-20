def main():
    import itertools
    (n, x, y) = list(map(int, input().split()))
    stat = [i for i in range(n)]
    ans = [0 for i in range(n - 1)]
    for s in itertools.combinations(stat, 2):
        d = min(s[1] - s[0], abs(x - 1 - s[0]) + 1 + abs(y - 1 - s[1]))
        ans[d - 1] += 1
    for i in range(len(ans)):
        print(ans[i])


def __starting_point():
    main()


__starting_point()
