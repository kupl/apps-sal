
n = int(input())
left = 0
right = 10 ** 10
while right - left > 1:
    mid = (right + left) // 2
    if mid * (mid + 1) <= 2 * n + 2:
        left = mid
    else:
        right = mid
print((n - left + 1))
