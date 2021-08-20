from math import ceil
(n, k) = map(int, input().split())
a = [int(i) for i in input().split()]


def is_ok(x):
    c = 0
    for i in a:
        c += ceil(i / x) - 1
        if c > k:
            return False
    return True


def binary_search(m):
    left = 0
    right = m + 1
    while left <= right:
        center = (left + right) // 2
        if right - left == 1:
            return right
        elif is_ok(center):
            right = center
        else:
            left = center


if k == 0:
    print(max(a))
else:
    print(binary_search(max(a)))
