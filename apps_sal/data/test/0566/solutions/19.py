(r, g, b) = sorted(map(int, input().split()))
left = 0
right = b + 1
while right - left > 1:
    m = (right + left) // 2
    if m + min(m, b - m) + r + g >= 3 * m:
        left = m
    else:
        right = m
print(left)
