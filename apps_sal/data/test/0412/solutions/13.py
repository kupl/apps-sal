n=int(input())
a=list(map(int,input().split()))
k=1
n=0
for i in range(len(a)):
    s=a[i]
    f=True
    while f:
        if s%(k*2)==0:
            k*=2
        else:
            f=False
    
for i in range(len(a)):
    if a[i]%k==0:
        n+=1
print(k,n)
        
        
    
    

