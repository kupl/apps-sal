def sq(x):
    l = 0
    r = 10**9 + 1
    while l + 1 < r:
        m = (l + r) // 2
        if m * (m + 1) // 2 <= x:
            l = m
        else:
            r = m
    return l


def s():
    [n, k] = list(map(int, input().split()))
    if k * (k - 1) // 2 + 1 < n:
        print(-1)
        return
    l = int(k * (k - 1) // 2) + 1 - n
    import math
    a = sq(l)
    print(k - 1 - a)


s()
