(n, m, k) = [int(i) for i in input().split(' ')]
if k < n:
    print(k + 1, 1)
else:
    k = k - n
    (level, remainder) = divmod(k, m - 1)
    x = n - level
    direction = level % 2
    if direction == 0:
        y = remainder + 2
    else:
        y = m - remainder
    print(x, y)
