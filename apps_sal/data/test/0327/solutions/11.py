def read():
    return list(map(int,input().split()))
n,k=read()
if k==1:
    print(n)
else:
    ans=0
    for i in range(len(bin(n)[2:])):
        ans+=2**i
    print(ans)
        
        

