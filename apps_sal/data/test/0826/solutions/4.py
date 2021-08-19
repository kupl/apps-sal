import sys


def is_match(k):
    if (1 + k) * k // 2 <= n + 1:
        return True
    else:
        return False


n = int(input())
left = -1
right = n + 1
while right - left > 1:
    mid = (left + right) // 2
    if is_match(mid):
        left = mid
    else:
        right = mid
print(n - left + 1)
