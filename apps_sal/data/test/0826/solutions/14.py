n = int(input())
left = 0
right = n + 1
while left < right - 1:
    mid = left + right >> 1
    if mid * (mid + 1) // 2 <= n + 1:
        left = mid
    else:
        right = mid
print(n + 1 - left)
