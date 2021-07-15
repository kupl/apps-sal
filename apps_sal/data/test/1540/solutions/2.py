n,m,k=map(int,input().split())
L=[]
for i in range(n):
    L.append(list((map(int,input().split()))))

K={}
for i in range(m):
    K[i+1]=[]
    for j in range(n):
        if(L[j][i]==1):
            K[i+1].append(j+1)
Ans=[0]*n
Anss=[0]*m
for i in range(k):
    x,y=map(int,input().split())
    Anss[y-1]+=1
    Ans[x-1]-=1
for i in range(n):
    for j in range(m):
        if(L[i][j]==1):
            Ans[i]+=Anss[j]
for item in Ans:
    print(item,end=" ")

