def v(length, start):
    W = start * (start + 1) // 2
    t = max(0, start - length)
    T = t * (t + 1) // 2
    return W - T + max(0, length - start)


def check(p):
    return p + v(k - 1, p - 1) + v(n - k, p - 1) <= m


n, m, k = map(int, input().split())
l = 0
r = 10 ** 100
while r - l > 1:
    mid = (l + r) // 2
    if not check(mid):
        r = mid
    else:
        l = mid
print(l)
