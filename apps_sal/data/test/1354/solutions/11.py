import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    (n, k, a) = mints()
    a += 1
    m = mint()
    x = list(mints())
    l = 0
    r = m + 1
    while r - l > 1:
        c = (l + r) // 2
        b = x[:c]
        b.sort()
        last = 0
        cnt = 0
        for i in b:
            if i != last:
                cnt += (i - last) // a
            last = i
        cnt += (n + 1 - last) // a
        if cnt < k:
            r = c
        else:
            l = c
    if r == m + 1:
        r = -1
    print(r)


solve()
