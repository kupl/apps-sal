def reach_max(n, k):
    return n * k + 1 - n * (n + 1) // 2


n, k = list(map(int, input().split()))

if n == 1:
    print(0)
    return

lo, hi = 1, k - 1

if n > reach_max(hi, k):
    print(-1)
    return


while lo < hi:
    mid = (lo + hi) // 2
    if reach_max(mid, k) < n:
        lo = mid + 1
    else:
        hi = mid

print(lo)

