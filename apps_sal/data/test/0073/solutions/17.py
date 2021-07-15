c, v0, v1, a, l = [int(i) for i in input().split()]
if v0 >= c:
    print(1)
    return
else:
    d = 1
    cnt = c - v0
    ca = 0
    while cnt > 0:
        ca += a
        cr = v0 + ca
        if cr > v1:
            cr = v1
        cnt -= (cr - l)
        d += 1
    print(d
          )
        

