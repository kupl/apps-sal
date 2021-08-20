n = int(input())
left = 0
right = n + 2
while left + 1 < right:
    m = (left + right) // 2
    if m * (m + 1) // 2 <= n + 1:
        left = m
    else:
        right = m
print(n + 1 - left)
