n = int(input())

a = [int(i) for i in input().split()]

a = sorted(a)
if len(a) == 1:
    print(-1)
elif len(a) == 2:
    d = a[1] - a[0]
    if d == 0:
        print(1)
        print(a[0])
        return
    elif d%2 == 0:
        print(3)
        print(a[0]-d,int(a[0]+d/2),a[1]+d)
        return
    else:
        print(2)
        print(a[0]-d,a[1]+d)
        return
else:
    d = a[1] - a[0]
    d2 = a[2] - a[1]
    
    if (d != d2):
        if len(a)>3:
            d = a[3] - a[2]
        else:
            d = min(d,d2)
    
    c = 0
    e = 0
    f = 0
    for i in range(len(a)-1):
        if a[i+1] - a[i] != d:
            e = a[i+1] - a[i]
            f = i
            c += 1
        if c == 2:
            print(0)
            return
    if c==0:
        if (d==0):
            print(1)
            print(a[0])
            return
        else:
            print(2)
            print(a[0]-d, a[len(a)-1]+d)
            return
    else:
        if e == 2*d:
            print(1)
            print(a[f]+d)
            return
        else:
            print(0)
            return
    
        
        

