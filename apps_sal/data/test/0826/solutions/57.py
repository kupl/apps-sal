n = int(input())
(left, right) = (0, 10 ** 18)
while right - left > 1:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= n + 1:
        left = mid
    else:
        right = mid
print(n - left + 1)
