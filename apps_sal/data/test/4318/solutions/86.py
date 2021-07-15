N=int(input())
H=list(map(int,input().split()))
ans=0
h=0
for i in range(N):
    if H[i]>=h:
        ans+=1
        h=H[i]
print(ans)

