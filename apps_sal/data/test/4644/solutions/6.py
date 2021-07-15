t=int(input())
while(t):
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    co=0
    for i in a:
        if(i%2):
            co+=1
    if((co==n and n%2==0) or co==0):
        print("NO")
    else:
        print("YES")

