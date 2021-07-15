n,k=map(int,input().split())

L=list(map(int,input().split()))

Taken=[False]*(n*k+1)

for item in L:
    Taken[item]=True
ind=1
for i in range(k):
    cnt=1
    print(L[i],end=" ")
    
    while(cnt<n):
        while(Taken[ind]):
            ind+=1
        
        print(ind,end=" ")
        ind+=1
        cnt+=1
    print()

