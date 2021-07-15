t=int(input())
for _ in range(t):
    n,x=list(map(int,input().split()))
    ar=list(map(int,input().split()))
    ar=set(ar)
    ans=1
    for i in range(1,1000):
        if(x==0):continue
        if(i not in ar):
            x-=1
            ar.add(i)
    i=1
    while(i in ar):i+=1
    print(i-1)

