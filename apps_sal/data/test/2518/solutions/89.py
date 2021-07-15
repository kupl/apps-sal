n, a, b = map(int, input().split())
h = [int(input()) for i in range(n)]
l, r = 0, max(h)
while l + 1 < r:
    m = (l + r) // 2
    cnt = 0
    for i in range(n):
        cnt += max(0, h[i] - b * m + a - b - 1) // (a - b)
    if cnt <= m:
        r = m
    else:
        l = m
print(r)
