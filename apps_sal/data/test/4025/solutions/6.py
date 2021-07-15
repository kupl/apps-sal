import copy
l=list(map(int,input().split()))
ans=min(l[0]//3,l[1]//2,l[2]//2)
l[0]-=ans*3
l[1]-=ans*2
l[2]-=ans*2
ans*=7
l1=[0,1,2,0,2,1,0]
l1+=l1
v=ans
for i in range(7) :
    k=0
    L=copy.copy(l)
    for j in range(i,i+7) :
        if L[l1[j]]<=0 :
            break
        L[l1[j]]-=1
        k+=1
    
    ans=max(ans,v+k)
print(ans)
    
    

