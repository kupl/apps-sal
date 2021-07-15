m,n=list(map(int,input().split()))
s=set(range(1,n+1))
d=[[None,None]for i in range(m)]
for i in range(m):
    x=list(map(int,input().split()))[1:]
    x=set(x)
    d[i][0]=x
    d[i][1]=s-x
for i in range(m):
    for j in range(i+1,m):
        bi,si=d[i]
        bj,sj=d[j]
        if sj.issuperset(bi) and bj.issubset(si):
            print('impossible')
            quit()
print('possible')

