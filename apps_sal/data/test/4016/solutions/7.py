n,m=list(map(int,input().split()))
s=input()
x=0
for i in range(1,n):
    if s[i::]==s[0:n-i]:
        x=n-i
        break
ans=s+s[x::]*(m-1)
print(ans)

