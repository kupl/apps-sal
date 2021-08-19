def main():
    from bisect import bisect
    (n, m, k) = list(map(int, input().split()))
    (t, s) = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    aa.append(t)
    bb = list(map(int, input().split()))
    bb.append(0)
    cc = [0, *list(map(int, input().split())), 0]
    dd = [0, *list(map(int, input().split())), s + 1]
    res = []
    for (t, b) in zip(aa, bb):
        b = s - b
        if b >= 0:
            i = bisect(dd, b)
            if b < dd[i]:
                i -= 1
            x = n - cc[i]
            if x <= 0:
                res = [0]
                break
            res.append(x * t)
    print(min(res))


def __starting_point():
    main()


__starting_point()
