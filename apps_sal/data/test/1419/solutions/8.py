def f(r):
    prev, ofs = -1, -1
    s = list()
    while True:
        try:
            ofs = r.index(' ', ofs + 1)
        except ValueError:
            s.append(len(r) - 1 - prev)
            return s
        s.append(ofs - prev)
        prev = ofs


n = int(input())
s = f(input().replace('-', ' '))


def can(w):
    cnt, cur = 0, 0
    for l in s:
        if l > w:
            return False
        ln = cur + l <= w
        cur = cur * ln + l
        cnt += not ln
    return cnt < n


def bsearch(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


print(bsearch(0, sum(s)))
