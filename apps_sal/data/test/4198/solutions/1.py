def resolve():
    a,b,x = map(int,input().split())
    l,r = 0, 10**9+1
    while l<r-1:
        m = l + (r-l)//2
        p = a*m+b*len(str(m))
        if p > x:
            r = m
        else:
            l = m
    print(l)
resolve()
