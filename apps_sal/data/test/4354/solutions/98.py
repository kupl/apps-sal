n,m =map(int,input().split())
a=[0]*n
b=[0]*n
c=[0]*m
d=[0]*m
for i in range(n):
    a[i],b[i]=map(int,input().split())
for i in range(m):
    c[i],d[i]=map(int,input().split())

for i in range(n):
    for j in range(m):
        if j==0:
            ind=0
            dis=abs(a[i]-c[j])+abs(b[i]-d[j])
        else:
            if abs(a[i]-c[j])+abs(b[i]-d[j])<dis:
                ind=j
                dis = abs(a[i] - c[j]) + abs(b[i] - d[j])
    print(ind+1)
