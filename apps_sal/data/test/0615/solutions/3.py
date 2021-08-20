def tmp(a, b, c):
    return (abs(a - b), abs(a - b + 2 * c))


def solve(string):
    (n, *a) = list(map(int, string.split()))
    (l, c, r) = (1, 2, 3)
    (sll, slr, srl, srr) = (sum(a[:l]), sum(a[l:c]), sum(a[c:r]), sum(a[r:]))
    ans = max(sll, slr, srl, srr) - min(sll, slr, srl, srr)
    while c < n - 1:
        (d, dn) = tmp(sll, slr, a[l])
        while dn < d:
            (sll, slr, l) = (sll + a[l], slr - a[l], l + 1)
            (d, dn) = tmp(sll, slr, a[l])
        (d, dn) = tmp(srl, srr, a[r])
        while dn < d:
            (srl, srr, r) = (srl + a[r], srr - a[r], r + 1)
            (d, dn) = tmp(srl, srr, a[r])
        ans = min(ans, max(sll, slr, srl, srr) - min(sll, slr, srl, srr))
        (slr, srl, c) = (slr + a[c], srl - a[c], c + 1)
    return str(ans)


def __starting_point():
    print(solve('\n'.join([input(), input()])))


__starting_point()
