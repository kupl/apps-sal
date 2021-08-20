def absdiff(a, b):
    return abs(b - a)


def solve(s):
    (n, *a) = list(map(int, s.split()))
    (l, r, ans) = (1, 3, sum(a))
    (sll, slr, srl, srr) = (a[0], 0, sum(a[1:3]), sum(a[3:]))
    for c in range(1, n - 1):
        slr += a[c]
        srl -= a[c]
        r = max(c, r)
        while l < c and absdiff(sll + a[l], slr - a[l]) < absdiff(sll, slr):
            (sll, slr, l) = (sll + a[l], slr - a[l], l + 1)
        while r < len(a) and absdiff(srl + a[r], srr - a[r]) < absdiff(srl, srr):
            (srl, srr, r) = (srl + a[r], srr - a[r], r + 1)
        (_max, _min) = (max(sll, slr, srl, srr), min(sll, slr, srl, srr))
        ans = min(ans, absdiff(_min, _max))
    return ans


print(solve('\n'.join([input(), input()])))
