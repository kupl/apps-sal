n, m, k = list(map(int, input().split()))


def __sum(n):
    return n * (n + 1) // 2


def _sum(l, r):
    if l > r:
        return 0
    delta = 0
    if l <= 0:
        delta = abs(l) + 1
        l = 1

    # print(l, r, __sum(r) - __sum(l - 1))
    return __sum(r) - __sum(l - 1) + delta


left = 1
right = int(1e9) + 2
while right - left > 1:
    mid = (left + right) // 2
    sub = _sum(mid - k + 1, mid) + _sum(mid - (n - k), mid - 1)
    if sub <= m:
        left = mid
    else:
        right = mid

print(left)
