def pillows(n, k, h):
    p = (h - 1) * h + h
    left = 0
    if k < h:
        left = (h - k) * (h - k + 1) // 2
    right = 0
    if n - k + 1 < h:
        right = (h - (n - k + 1)) * (h - (n - k + 1) + 1) // 2

    return p - left - right


def solve(n, m, k):
    p = m - n
    if p == 0:
        return 1

    l = 0
    r = 10**10
    while r - l >= 2:
        m = (l + r) // 2
        mp = pillows(n, k, m)
        if mp > p:
            r = m
        else:
            l = m

    return l + 1

if False:
    assert pillows(1, 1, 10) == 10
    assert solve(1, 10, 1) == 10
    assert solve(5, 5, 1) == 1
    assert solve(5, 5, 5) == 1
    assert solve(5, 5, 3) == 1
    assert solve(5, 6, 2) == 2
    assert solve(5, 6, 1) == 2
    assert solve(5, 6, 5) == 2
    assert solve(5, 7, 5) == 2
    assert solve(5, 7, 1) == 2
    assert solve(5, 8, 1) == 3
    assert solve(5, 8, 5) == 3
    assert solve(5, 8, 4) == 2
    assert solve(5, 8, 2) == 2
    assert solve(5, 8, 3) == 2
    assert solve(5, 9, 3) == 3
    assert solve(5, 9, 2) == 3
    assert solve(5, 9, 1) == 3

else:
    n, m, k = list(map(int, input().split()))
    print(solve(n, m, k))

