def solve(string):
    n, *a = list(map(int, string.split()))
    l, c, r = 1, 2, 3
    sll, slr, srl, srr = sum(a[:l]), sum(a[l:c]), sum(a[c:r]), sum(a[r:])
    ans = max(sll, slr, srl, srr) - min(sll, slr, srl, srr)
    while c < n - 1:
        d = abs(sll - slr)
        dn = abs(sll + 2 * a[l] - slr)
        while dn < d:
            sll, slr = sll + a[l], slr - a[l]
            l += 1
            d = abs(sll - slr)
            dn = abs(sll + 2 * a[l] - slr)
        d = abs(srl - srr)
        dn = abs(srl + 2 * a[r] - srr)
        while dn < d:
            srl, srr = srl + a[r], srr - a[r]
            r += 1
            d = abs(srl - srr)
            dn = abs(srl + 2 * a[r] - srr)
        ans = min(ans, max(sll, slr, srl, srr) - min(sll, slr, srl, srr))
        slr += a[c]
        srl -= a[c]
        c += 1
    return str(ans)


def __starting_point():
    print((solve('\n'.join([input(), input()]))))

__starting_point()
