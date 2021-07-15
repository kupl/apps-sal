from itertools import accumulate


def solve(string):
    n, *a = list(map(int, string.split()))
    *a, = accumulate(a)
    l, c, r = 0, 1, 2
    sll, slr, srl, srr = a[l], a[c] - a[l], a[r] - a[c], a[-1] - a[r]
    ans = max(sll, slr, srl, srr) - min(sll, slr, srl, srr)
    while c < n - 1:
        while abs(a[c] - 2 * a[l + 1]) < abs(a[c] - 2 * a[l]):
            l += 1
        while abs(a[-1] + a[c] - 2 * a[r + 1]) < abs(a[-1] + a[c] - 2 * a[r]):
            r += 1
        sll, slr, srl, srr = a[l], a[c] - a[l], a[r] - a[c], a[-1] - a[r]
        ans = min(ans, max(sll, slr, srl, srr) - min(sll, slr, srl, srr))
        c+=1
    return str(ans)


def __starting_point():
    print((solve('\n'.join([input(), input()]))))

__starting_point()
