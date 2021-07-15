n,t=list(map(int, input().split()))
ct=[list(map(int, input().split())) for i in range(n)]
c=[]
for i in range(n):
    if ct[i][1]<=t:
        c.append(ct[i][0])
print((min(c) if len(c)!=0 else "TLE"))

