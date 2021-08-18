n = int(input())
x = 1
while True:
    l = 0
    r = 10 ** 18
    while r > l + 1:
        m = (l + r) // 2
        if x * m < n:
            l = m
        else:
            r = m
    if r * x > n:
        print(r)
        return
    x *= 3
