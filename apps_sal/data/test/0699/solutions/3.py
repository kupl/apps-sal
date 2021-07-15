y,k,n=map(int,input().split())

a=(k-(y%k))%k
if(a==0):
    a+=k
done=False
while(a+y<=n):
    print(a,end=" ")
    done=True
    a+=k
if(not done):
    print(-1)

