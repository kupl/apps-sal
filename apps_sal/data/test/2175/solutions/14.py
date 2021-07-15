n=int(input())
a=[int(i) for i in input().split()]
v=[0]*n
m=int(input())
f=[i+1 for i in range(n)]
ans=[]
for i in range(m):
    q=[int(i) for i in input().split()]
    if q[0]==1:
        p,x=q[1],q[2]
        xyz=[]
        j=p-1
        while j<n:
            tmp=x+v[j]-a[j]
            if tmp<=0:
                v[j] = x+v[j]
                break
            else:
                x=tmp
                v[j]=a[j]
                xyz.append(j)
                j=f[j]
        for z in xyz:
            f[z]=j
    else:
        ans.append(v[q[1]-1])

for i in ans:
    print(i)
