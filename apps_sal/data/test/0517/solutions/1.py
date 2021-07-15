n,d,h = (int(i) for i in input().split())
if h*2 < d or n < d+1 or d == 1 and n > 2 :
    print(-1)
else:
    for i in range(h):
        print(i+1,i+2)
    ost = h+1
    if d > h:
        print(1,ost+1)
    for i in range(d-h-1):
        print(ost+i+1,ost+i+2)
    if d != h:
        for i in range(1,n-d):
            print(1,d+1+i)
    else:
        for i in range(1,n-d):
            print(2,d+1+i)


