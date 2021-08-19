def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


(N, H) = mi()
tar = N + H * (H - 1) // 2
(lo, hi) = (H, tar)
while lo < hi:
    mid = (lo + hi + 1) // 2
    if mid * mid <= tar:
        lo = mid
    else:
        hi = mid - 1
if lo * lo == tar:
    ans = 2 * lo - H
elif lo * lo > tar:
    (lo1, hi1) = (1, N)
    while lo1 < hi1:
        mid1 = (lo1 + hi1 + 1) // 2
        if mid1 * (mid1 + 1) // 2 <= N:
            lo1 = mid1
        else:
            hi1 = mid1 - 1
    ans = lo1
    if lo1 * (lo1 + 1) // 2 < N:
        ans += 1
else:
    dif = tar - lo * lo
    if dif <= lo:
        ans = 2 * lo - H + 1
    else:
        ans = 2 * lo - H + 2
print(ans)
