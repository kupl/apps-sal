import sys
input = sys.stdin.readline
for f in range(int(input())):
    n,m=list(map(int,input().split()))
    neig=[0]*n
    for i in range(n):
        neig[i]=[0]
    
    for i in range(m):
        a,b=list(map(int,input().split()))
        a-=1
        b-=1
        neig[a][0]+=1
        neig[a].append(b)
    lev=[1]*n
    for i in range(n):
        for j in range(1,neig[i][0]+1):
            x=lev[i]+1
            if x==4:
                x=1
            lev[neig[i][j]]=max(lev[neig[i][j]],x)
    sol=0
    s=[]
    for i in range(n):
        if lev[i]==3:
            sol+=1
            s.append(i+1)
    print(sol)
    print(*s)
    

