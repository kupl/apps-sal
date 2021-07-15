n = int(input())
if n <= 2:
    print(1)
else:
    l, r = 0, n
    d = (l + r) // 2
    while r - l > 1:
        if d * (d + 1) <= 2 * (n + 1):
            l = d
        else:
            r = d
        d = (l + r) // 2
    print(n-d+1)
