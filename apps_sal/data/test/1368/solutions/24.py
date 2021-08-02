from operator import mul
from functools import reduce


def sml_cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    n, a, b = map(int, input().split())
    v = list(map(int, input().split()))
    v.sort()
    ave = 0
    for i in range(1, a + 1):
        ave += v[n - i]
    ave /= a
    l, r = -1, -1
    target = v[n - a]
    for i in range(n):
        if v[i] == target:
            l = i
            break
    for i in reversed(range(n)):
        if v[i] == target:
            r = i
            break
    cnt = r - l + 1
    high, low = min(cnt, r - (n - b) + 1), r - (n - a) + 1
    ans = sml_cmb(cnt, low)
    if v[n - a] == v[n - 1]:
        for i in range(low + 1, high + 1):
            ans += sml_cmb(cnt, i)
    print(ave)
    print(ans)


def __starting_point():
    main()


__starting_point()
