n,k=list(map(int,input().split()))
ans=[1]*n
for i in range(k):
    s=int(input())
    l=list(map(int,input().split()))
    for j in range(s):
        if ans[l[j]-1]==1:
            ans[l[j]-1]=0
print((sum(ans)))
            
        
        

