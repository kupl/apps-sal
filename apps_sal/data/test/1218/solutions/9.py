n, k = list(map(int, input().split()))

l, h = int(-1), k + 1
while l + 1 < h:
    mid = (l + h) // 2
    val = (k - mid + 1 + k) * mid // 2 - (mid - 1)
    if val < n:
        l = mid
    else:
        h = mid

print(-1 if h == k + 1 else h)
