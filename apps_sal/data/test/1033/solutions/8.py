n, H = map(int, input().split())


def f(len, H):
    if len <= H:
        return len * (len + 1) // 2
    if (len - H) % 2 == 1:
        x = H + (len - H) // 2
        c = (len - H) // 2 + 1
        return c * (H + x) // 2 + x * (x + 1) // 2
    x = H + (len - H) // 2
    c = (len - H) // 2 + 1
    return c * (H + x) // 2 + x * (x - 1) // 2


lo, hi = 1, 1000000000000000000
while lo < hi:
    mid = (lo + hi) // 2
    if n > f(mid, H):
        lo = mid + 1
    else:
        hi = mid
print(lo)
