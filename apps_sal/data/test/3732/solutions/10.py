(x, y, m) = list(map(int, input().split()))
if max(x, y) >= m:
    print(0)
elif m < 0 or max(x, y) <= 0:
    print(-1)
else:
    if x + y < 0:
        cnt = (max(x, y) - min(x, y)) // max(x, y)
        (x, y) = (min(x, y) + max(x, y) * cnt, max(x, y))
    else:
        cnt = 0
    while max(x, y) < m:
        (x, y) = (max(x, y), x + y)
        cnt += 1
    print(cnt)
