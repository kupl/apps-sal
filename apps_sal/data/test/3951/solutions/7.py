def main():
    from collections import Counter
    from math import gcd, sqrt
    n = int(input())
    cnt = Counter(list(map(int, input().split())))
    kk = sorted(list(cnt.keys()), reverse=True)
    res = []
    for k in kk:
        c = Counter()
        for (k0, v0) in res:
            q = gcd(k, k0)
            c[q] += v0
        b = c[k]
        del c[k]
        v = int(sqrt(b * b + cnt[k])) - b
        res.append((k, v))
        for (k0, v0) in list(c.items()):
            cnt[k0] -= v0 * v * 2
    print(*sorted((k for (k, v) in res for _ in range(v))))


def __starting_point():
    main()


__starting_point()
