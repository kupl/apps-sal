def mySqrt(n):
    l = 0
    r = n + 1
    while (l < r - 1):
        m = (l + r) // 2
        if m * m > n:
            r = m
        else:
            l = m
    return l


n, m = [int(i) for i in input().split()]

if m >= n:
    print(n)
else:
    ans = m
    d = (-1 + mySqrt(1 + 8 * (n - m))) // 2
    while d * (d - 1) // 2 + d + m >= n:
        d -= 1
    while d * (d - 1) // 2 + d + m < n:
        d += 1
    print(m + d)
