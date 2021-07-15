a,b=list(map(int,input().split()))
mid=(int)(a/2+a%2)
if b<=mid:
    print(b*2-1)
else:
    N=(int)(b-mid)*2
    print(N)

