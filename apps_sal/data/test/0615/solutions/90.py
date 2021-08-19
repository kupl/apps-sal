from itertools import accumulate


def solve(string):
    (n, *a) = list(map(int, string.split()))
    (*a,) = accumulate(a)
    (l, r, e, ans) = (0, 2, a[-1], a[-1])
    for c in a[1:-2]:
        while a[l] + a[l + 1] < c:
            l += 1
        while a[r] + a[r + 1] < c + e:
            r += 1
        t = sorted([a[l], c - a[l], a[r] - c, e - a[r]])
        ans = min(ans, t[-1] - t[0])
    return str(ans)


def __starting_point():
    print(solve('\n'.join([input(), input()])))


__starting_point()
