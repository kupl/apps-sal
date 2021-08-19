def main():
    n = int(input())
    aa = list(map(int, input().split()))
    aa.sort()
    lim = aa[-1] + 1
    (cnt, a) = ([0] * lim, aa[0] - 1)
    for (i, b) in zip(list(range(n, -1, -1)), aa):
        if a != b:
            cnt[a + 1:b + 1] = [i] * (b - a)
            a = b
    (avail, res) = ([True] * lim, [])
    for (i, a) in enumerate(aa):
        if avail[a]:
            avail[a] = False
            res.append(a * sum(cnt[a::a]))
    print(max(res))


def __starting_point():
    main()


__starting_point()
