n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
l, r = 0, n
while r - l > 1:
    m = (r + l) // 2
    if a[m] > 5 - k:
        r = m
    else:
        l = m
print((l + 1) // 3)
