a,b,c=list(map(int,input().split()))
d=0
def ans(a,b,c,d):
    if c%a==0 or c%b==0:
        print('Yes')
        return
    else:
        a,b=min(a,b),max(a,b)
        ##print(a,b)
        while d<c:
            d+=a
            if (c-d)%b==0:
                print('Yes')
                return
            else:
                continue
        print("No")
        return
ans(a,b,c,d)

