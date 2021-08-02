n = int(input())

left = 0
right = n + 2
while left + 1 < right:
    m = (left + right) // 2
    if m * (m + 1) // 2 <= n + 1:
        left = m
    else:  # ng
        right = m
# 1....left = n + 1
print((n + 1 - left))
