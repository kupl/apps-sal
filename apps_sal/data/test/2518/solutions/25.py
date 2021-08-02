import math
n, a, b = map(int, input().split())
h = [int(input()) for i in range(n)]
l, r = 0, 10**9
while r - l > 1:
    m = (l + r) // 2
    count = 0
    for i in h:
        count += max(math.ceil((i - b * m) / (a - b)), 0)
    if count <= m:
        r = m
    else:
        l = m
print(r)
