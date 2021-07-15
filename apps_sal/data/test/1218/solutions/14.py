R = lambda: map(int, input().split())
n, k = R()
if n == 1:
    print(0)
    return
if 1 + k * (k - 1) // 2 < n:
    print(-1)
    return
l, r = 0, k - 1
while l < r:
    m = (l + r + 1) // 2
    if 1 + (m + k - 1) * (k - 1 - m + 1) // 2 >= n:
        l = m
    else:
        r = m - 1
if 1 + (l + k - 1) * ((k - 1) - l + 1) // 2 < n:
    print(k - 1 - l + 2)
else:
    print(k - 1 - l + 1)
