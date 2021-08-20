t = int(input())
while t > 0:
    s = 0
    g = 0
    p = 0
    (a, b, c, d) = input().strip().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    for i in range(a, b + 1):
        if d > i:
            p = d - i
            s = s + p
        if c > i:
            g = c - i
            s = s - g + 1
    print(s)
    t -= 1
