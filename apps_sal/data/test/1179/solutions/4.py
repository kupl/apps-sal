(n, k) = map(int, input().split())
a = list(map(int, input().split()))
(l, r) = (0, n)
while r - l > 1:
    m = (r + l) // 2
    s = m * (m + 1) // 2
    if s < k:
        l = m
    else:
        r = m
k -= l * (l + 1) // 2
print(a[k - 1])
