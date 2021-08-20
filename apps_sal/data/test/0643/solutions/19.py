t = int(input())
for i in range(t):
    (x, y, p, q) = list(map(int, input().split()))
    left = -1
    right = 10 ** 9
    r = right
    while left + 1 < right:
        t = (left + right) // 2
        if p * t >= x and q * t - p * t >= y - x:
            right = t
        else:
            left = t
    if not (p * r >= x and q * r - p * r >= y - x):
        print(-1)
    else:
        print(q * right - y)
