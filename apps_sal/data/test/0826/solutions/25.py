n = int(input())
left = 0
right = 10 ** 10
while left + 1 < right:
    mid = (left + right) // 2
    now = mid * (mid + 1) // 2
    if now <= n + 1:
        left = mid
    else:
        right = mid
print(n - left + 1)
