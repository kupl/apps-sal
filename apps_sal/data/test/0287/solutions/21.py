(n, m) = list(map(int, input().split()))
if m <= 0 or m >= n:
    a = 0
else:
    a = 1
b = 0
if m > 0:
    if m * 2 <= n:
        if n % 2 == 0 and m >= n // 2:
            b = max(b, m)
        else:
            b = max(b, m + 1)
    else:
        b = max(b, n - n // 2 - (m - n // 2))
    if m * 3 <= n:
        b = max(b, m * 2)
    else:
        b = max(b, n // 3 * 2 - (m - n // 3 - n % 3))
print(a, b)
