from sys import stdin
c=int(stdin.readline().strip())
for i in range(c):
    n,m=list(map(int,stdin.readline().strip().split()))
    s=[stdin.readline().strip() for j in range(n)]
    ms=[]
    ns=[]
    for j in range(n):
        ns.append(s[j].count("."))
    
    for j in range(m):
        ms.append(0)
        for k in range(n):
            if s[k][j]==".":
                ms[-1]+=1
    ans=10**15
    for j in range(n):
        for k in range(m):
            x=ns[j]+ms[k]
            if s[j][k]==".":
                x-=1
            ans=min(ans,x)
    print(ans)

