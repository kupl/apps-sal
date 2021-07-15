for _ in range(int(input())):
    a,b,c,r=map(int,input().split())
    a,b=min(a,b),max(a,b)
    n = b - a
    l,f = c-r,c+r
    if a>l:
        a,b,l,f=l,f,a,b
    # print (a,b,l,f)

    if l >= b:
        print (n)
    else:
        if f <= b:
            print (n - (f - l))
        else:
            print (n - (b - l))
