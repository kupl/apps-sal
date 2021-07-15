t = int(input())
while t>0:
    t-=1
    a,b,c,r = map(int,input().split())
    if a>b:
        a,b=b,a
    print(min(max((c-r)-a,0)+max(b-(c+r),0),abs(b-a)))
