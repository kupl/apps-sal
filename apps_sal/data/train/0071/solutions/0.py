t=int(input())
while t>0 :
    n=int(input())
    a=list(map(int,input().split()))
    an=0
    s=0
    for i in a :
        if s+i>=0 :
            s+=i 
        else :
            s+=i
            an-=s 
            s=0
    print(an)
    t-=1 
