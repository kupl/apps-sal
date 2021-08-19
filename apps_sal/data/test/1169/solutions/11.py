(n, m) = map(int, input().split())
print(max(0, n - 2 * m), end=' ')
l = -1
r = n + 1
while r - l > 1:
    s = (l + r) // 2
    if s * (s - 1) < 2 * m:
        l = s
    else:
        r = s
print(max(0, n - r))
