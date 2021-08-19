t = int(input())
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    (l, r) = (0, min(a, b) + 1)
    while r - l > 1:
        m = (l + r) // 2
        if a - m + b - m >= m:
            l = m
        else:
            r = m
    print(l)
