T = int(input())
for _ in range(T):
    (h, c, t) = list(map(int, input().split()))
    if h + c >= t * 2:
        print(2)
    else:
        (l, r) = (0, 10 ** 9)
        while r - l > 1:
            m = (l + r) // 2
            if h * (m + 1) + c * m >= t * (2 * m + 1):
                l = m
            else:
                r = m
        if (2 * l + 1) * ((2 * r + 1) * t - (h * (r + 1) + c * r)) >= (2 * r + 1) * (h * (l + 1) + c * l - (2 * l + 1) * t):
            print(l * 2 + 1)
        else:
            print(r * 2 + 1)
