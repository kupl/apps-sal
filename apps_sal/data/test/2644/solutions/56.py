n=int(input())
p=list(map(int,input().split()))
ans=[]
kensa=set()
count=0
for i in range(1,n):
    j=i
    while j-1>=0 and  p[j-1]>p[j]:
        if j in kensa:
            print(-1)
            return
        ans.append(j)
        kensa.add(j)
        count+=1
        p[j-1],p[j]=p[j],p[j-1]
        j-=1
    if count>=n:
        print(-1)
        return
if len(ans)==n-1:
    for j in ans:
        print(j)
else:
    print(-1)
