R=lambda:list(map(int,input().split()))
n,k=R()
if k==1:print(n)
else:
    i=0
    while (1<<i)<=n:i+=1
    print((1<<i)-1)

