(n, S) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
(lo, hi) = (0, n + 1)
while lo < hi:
    mid = (lo + hi) // 2
    if mid > n:
        hi = mid
        continue
    if sum(sorted((x + (i + 1) * mid for (i, x) in enumerate(a)))[:mid]) <= S:
        lo = mid + 1
    else:
        hi = mid
lo -= 1
print(lo, sum(sorted((x + (i + 1) * lo for (i, x) in enumerate(a)))[:lo]))
