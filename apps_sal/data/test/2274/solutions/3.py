t = int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(input())
    ans=0
    for i in range(n-1):
        if l[i][-1]!='D':
            ans+=1
    for i in range(m-1):
        if l[-1][i]!='R':
            ans+=1
    print(ans)
