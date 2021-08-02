import math
n, k = list(map(int, input().split()))
lst = list(map(int, input().split()))
l = 1
r = min(2 * (10 ** 9) + 1, n * (n + 1) / 2)
while (r > l):
    m = math.floor((l + r) / 2)
    if (m + 1) / 2 * m < k:
        l = m + 1
    else:
        r = m
print(lst[k - int(l * (l - 1) / 2) - 1])
