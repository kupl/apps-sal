(n, k) = map(int, input().split())
size = list(map(int, input().split()))
l = size[-1] - 1
r = size[-1] * 2
while r - l > 1:
    m = (r + l) // 2
    (x1, x2) = (0, len(size) - 1)
    cnt = 0
    while x1 <= x2:
        if size[x1] + size[x2] <= m:
            x1 += 1
            x2 -= 1
        else:
            x2 -= 1
        cnt += 1
    if cnt <= k:
        r = m
    else:
        l = m
print(r)
