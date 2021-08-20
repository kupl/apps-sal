def f(i, fd, m, n):
    return i * (i + 1) // 2 - fd * (fd - 1) // 2 >= (i - fd) * m + n


def solve(n, m):
    if m >= n:
        return n
    fd = m
    l = fd
    r = max(n, m) + 100
    while l < r:
        mid = (l + r) // 2
        if f(mid, fd, m, n):
            r = mid
        else:
            l = mid + 1
        if l == r - 1:
            if f(l, fd, m, n):
                r = l
            else:
                l = r
    return l


def brute(n, m):
    i = 1
    cur = n
    while True:
        cur += m
        cur = min(cur, n)
        cur -= i
        if cur <= 0:
            break
        i += 1
    return i


(n, m) = map(int, input().split())
print(solve(n, m))
