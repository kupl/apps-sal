n=int(input())
m=10**10
n=1
*a,=list(map(int,input().split()))
a.sort()
for i in range(1,len(a)):
    t=a[i]-a[i-1]
    if t<m:
        c=1
        m=t
    elif t==m:
        c+=1
print(m,c)

