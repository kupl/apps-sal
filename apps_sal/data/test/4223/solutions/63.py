N=int(input())
S=list(map(str,input()))
ans=1
for i in range(N-1):
    if S[i]!=S[i+1]:
        ans+=1
print(ans)
