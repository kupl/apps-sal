s=input().split()
n,h,a,b,k=int(s[0]),int(s[1]),int(s[2]),int(s[3]),int(s[4])
for que in range(k):
    s=input().split()
    ta,fa,tb,fb=int(s[0]),int(s[1]),int(s[2]),int(s[3])
    if ta==tb:
        print(abs(fa-fb))
    else:
        if a<=fa<=b:
            print(abs(fa-fb)+abs(ta-tb))
        elif fa<a:
            print(abs(a-fa)+abs(a-fb)+abs(ta-tb))
        elif fa>b:
            print(abs(b-fa)+abs(b-fb)+abs(ta-tb))

