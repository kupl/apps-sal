n, m = list(map(int, input().split()))

if n >= 2:
    even = n * (n - 1) / 2
else:
    even = 0

if m >= 2:
    odd = m * (m - 1) / 2
else:
    odd = 0

print((int(even + odd)))
