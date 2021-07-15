n=int(input())
L=[]
for i in range(n):
    l=list(input().split())
    for j in range(2): l[j]=int(l[j])
    L.append(l)
ans=0
for i in range(n):
    exist=False
    for j in range(n):
        if L[i][0]==L[j][1] and i!=j:
            exist=True
            break
    if not(exist): ans+=1
print(ans)
