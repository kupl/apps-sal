c, d = map(int, input().split())
n, m = map(int, input().split())
k = int(input())
x = n * m
if k >= x:
    print(0)
    return
if c <= d:
    div, mod = (x - k) // n, (x - k) % n
    if mod > 0:
        div += 1
    print(div * c)
else:
    if d * n <= c:
        print((x - k) * d)
    else:
        res = (x - k) // n * c
        mod = (x - k) % n
        if c < mod * d:
            res += c
        else:
            res += mod * d
        print(res)
