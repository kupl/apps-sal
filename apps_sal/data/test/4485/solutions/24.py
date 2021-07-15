N,M=list(map(int,input().split()))
nekotyann=[0]*N
wanntyann=[0]*N
ans="IMPOSSIBLE"
for i in range(M):
    a,b=list(map(int,input().split()))
    if a==1:
        nekotyann[b-1]+=1
    if b==N:
        wanntyann[a-1]+=1
for k in range(N):
    if nekotyann[k]!=0 and wanntyann[k]!=0:
        ans="POSSIBLE"
        break
print(ans)

