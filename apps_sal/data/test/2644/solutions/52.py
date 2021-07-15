n=int(input())
t=list(map(int,input().split()))
t=[-1]+t
pos=1
sol=[]
for i in range(1,n+1):
    if t[i]==pos:
        for j in range(i-1,pos-1,-1):
            sol.append(j)
            tmp=t[j]
            t[j]=t[j+1]
            t[j+1]=tmp
        pos=i      
for i in range(1,n+1):
    if t[i]!=i:
        print((-1))
        return
if len(sol)!=n-1:
    print((-1))
else:
    for i in sol:
        print(i)


