n,q=[int(i) for i in input().split()]
s=input()


dp=[0]*(n)
ans=0
for i in range(1,n):
    if s[i-1]=="A" and s[i]=="C":
        ans=ans+1
    dp[i]=ans

for i in range(q):
    l,r=[int(i) for i in input().split()]
    print((dp[r-1]-dp[l-1]))

