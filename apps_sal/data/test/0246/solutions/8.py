from math import ceil
n, s = [int(i) for i in input().split()]

l = 0
r = 10000000000000000000

while l < r:
    cur = (l + r) // 2
    sm = sum([int(i) for i in str(cur)])
    if cur - sm >= s:
        r = cur
    else:
        l = cur + 1

print(max(0, n - l + 1))

