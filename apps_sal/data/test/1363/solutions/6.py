(g, d, f) = map(int, input().split())
gg = list(map(int, input().split()))
dd = list(map(int, input().split()))
ff = list(map(int, input().split()))
gg.sort()
dd.sort()
ff.sort()


def get_kolvo(left, right, lst):
    l = -1
    r = len(lst)
    while r - l > 1:
        m = (r + l) // 2
        if lst[m] >= left:
            r = m
        else:
            l = m
    ql = r
    l = -1
    r = len(lst)
    while r - l > 1:
        m = (r + l) // 2
        if lst[m] > right:
            r = m
        else:
            l = m
    qr = l
    return qr - ql + 1


def c(n, k):
    if k == 1:
        return n
    elif k == 2:
        return n * (n - 1) // 2
    elif k == 3:
        return n * (n - 1) * (n - 2) // 6


def get(l, r):
    return c(get_kolvo(l, r, gg), 1) * c(get_kolvo(l, r, dd), 2) * c(get_kolvo(l, r, ff), 3)


ans = 0
for i in range(4, 100001):
    ans += get(i, 2 * i) - get(i, 2 * i - 2)
print(ans)
