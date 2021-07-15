n,m=list(map(int,input().split()))
s1=list(map(int,input().split()))
a=[0]*m
for i in range (n):
    a[s1[i]-1]+=1
kol=0
for i in range (m-1):
    for j in range (i+1,m):
        kol=kol+a[i]*a[j]
print(kol)

