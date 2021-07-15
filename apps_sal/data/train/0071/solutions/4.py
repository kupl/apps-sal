for _ in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    r=0
    avl=0
    for i in a:
        if i>0:
            avl+=i
        else:
            i=abs(i)
            d=min(avl,i)
            avl-=d
            r+=i-d
    print(r)
