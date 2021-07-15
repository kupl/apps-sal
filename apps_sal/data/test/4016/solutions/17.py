n,m=map(int,input().strip().split())
r=input()
ans=""
ans1=""
for i in range(n-1):
    if r[:i+1]==r[n-1-i:]:
        ans=r[:i+1]
j=len(ans)
ans1=r+(m-1)*r[j:]
print(ans1)
