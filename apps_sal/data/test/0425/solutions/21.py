n, p = map(int,input().split())
m = 10000000000
q = 0
for i in range(1, 100):
    a = n - i * p
    if a > 0:
        u = a
        o = 0
        while u > 0:
            if u % 2 == 1:
                o += 1
                u //= 2
            else:
                u //= 2
    
        mi = o
        if (i >= mi) and (a >= i):
            print(i)
            q = 1
            break
    else:
        break
if q == 0:
    print(-1)
