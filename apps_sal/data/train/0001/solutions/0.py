q=int(input())

for e in range(q):
    x,y,k=list(map(int,input().split()))
    x,y=abs(x),abs(y)
    x,y=max(x,y),min(x,y)
    
    if(x%2!=k%2):
        k-=1
        y-=1
    
    
    if(x>k):
        print(-1)
        continue
    if((x-y)%2):
        k-=1
        x-=1
    print(k)
    
    
    

