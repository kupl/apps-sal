m,n=map(int,input().split())
s=[0]*n
for i in range(m):
    a=list(map(int,input().split()))
    s[0]=s[0]+a[0]
    for j in range(1,n):
        s[j]=max(s[j-1],s[j])+a[j]
    print(s[-1],end=' ')

