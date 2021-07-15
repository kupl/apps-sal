def doit():
    x, y, m = [int(k) for k in input().strip().split()]
    if x < y:
        x, y = y, x
    if x >= m:
        print(0)
        return

    if x<=0 and y<=0:
        print(-1)
        return

    k = 0
    if y < 0:
        k = (-y+x-1)//x
        y += k*x
        assert(y >= 0)
    if x < y:
        x, y = y, x
        
    while x < m:
        k += 1
        x, y = x+y, x
        if x < y:
            x, y = y, x
    print(k)

doit()

