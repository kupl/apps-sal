import math
(n, k) = (int(x) for x in input().split())
An = [int(i) for i in input().split()]
left = 0
right = max(An)


def check(x):
    chk = 0
    for i in range(n):
        chk += math.ceil(An[i] / x) - 1
    return chk


while right - left != 1:
    x = (left + right) // 2
    if check(x) <= k:
        right = x
    else:
        left = x
print(right)
