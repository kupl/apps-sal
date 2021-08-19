import math
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
right = max(a)
left = 0


def cutable(a, x):
    count = 0
    for i in a:
        count += math.ceil(i / x) - 1
    return count <= k


while right > left + 1:
    mid = (right + left) // 2
    if cutable(a, mid):
        right = mid
    else:
        left = mid
print(right)
