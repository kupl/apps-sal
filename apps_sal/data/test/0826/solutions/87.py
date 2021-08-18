n = int(input())


def check(k):
    return k * (k + 1) // 2 <= n + 1


left = 0
right = 10 ** 18 + 1

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print((n - left + 1))
