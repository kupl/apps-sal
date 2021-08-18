from decimal import Decimal
n = int(input())


left = 0
right = n + 1
mid = (left + right) // 2

for _ in range(100000):

    mid = (left + right) // 2

    if mid * (mid + 1) // 2 > n + 1:
        right = mid

    else:
        left = mid

i = mid


print((n - i + 1))
