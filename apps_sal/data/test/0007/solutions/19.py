(n, m) = map(int, input().split())
tl = m
tr = n
while tr - tl > 1:
    mid = (tr + tl) // 2
    val = (mid - m) * (mid - m + 1) // 2
    bef = (mid - m) * (mid - m - 1) // 2
    if val >= n or n - bef <= mid:
        tr = mid
    else:
        tl = mid
print(tr)
