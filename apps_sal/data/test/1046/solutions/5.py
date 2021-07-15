n=int(input())

C={}

L=list(map(int,input().split()))

for i in range(n):
    item=L[i]
    if(item in C):
        C[item].append(i)
    else:
        C[item]=[i]
valid=True
ans=0
for item in C:
    if(item==0):
        continue
    if(len(C[item])>2):
        valid=False
        ans=-1
        break
    if(len(C[item])==2):
       ans+=1

print(ans)

