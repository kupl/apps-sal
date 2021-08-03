n = int(input().strip())

r = 10**19
l = 0
m = 0
while l + 1 < r:
    m = (l + r) >> 1
    if m * (1 + m) >> 1 <= n + 1:
        l = m
    else:
        r = m

print(n - l + 1)
