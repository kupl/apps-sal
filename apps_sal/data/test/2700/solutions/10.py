t = int(input())
while t > 0:
    s = 0
    g = 0
    p = 0
    a, b, c, d = input().strip().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    for i in range(a, b + 1):
        # print i,
        if d > i:
            p = (d - i)
            # print p,
            s = s + p
        # print s,
        if c > i:
            g = (c - i)
            # print g,
            s = s - g + 1
        # print s
    print(s)
    t -= 1
