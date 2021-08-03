n = int(input())
l = 0
r = n
while r - l > 1:
    m = (l + r) // 2
    if m * m >= n:
        r = m
    else:
        l = m
if (r - 1) * r >= n:
    print(2 * r - 1)
else:
    print(2 * r)
