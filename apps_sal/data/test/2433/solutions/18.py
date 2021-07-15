from sys import stdin
n=int(stdin.readline().strip())
for i in range(n):
    v,p,f=list(map(int,stdin.readline().strip().split()))
    h,c=list(map(int,stdin.readline().strip().split()))
    ans=0
    for j in range(101):
        for k in range(101):
            v1,p1,f1=v,p,f
            v1-=2*j
            p1-=j
            v1-=2*k
            f1-=k
            if(v1>=0 and p1>=0 and f1>=0):
                ans=max(ans,h*j+c*k)
    print(ans)
            

