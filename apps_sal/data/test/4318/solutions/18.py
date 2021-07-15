N=int(input())
H=list(map(int,input().split()))
temp=0
ans=0
for i in range(N):
    if temp<=H[i]:
        ans+=1
        temp=H[i]
print(ans)

