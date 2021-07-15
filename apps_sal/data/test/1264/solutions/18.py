n=int(input())
a=list(map(int,input().split()))


ans=-n
for i in range(n):
    for j in range(i,n):
        u=j-i+1-2*a[i:j+1].count(1)
        if u>ans:
            ans=u
           #print(i,j,ans)

print(a.count(1)+ans)

