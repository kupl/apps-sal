N=int(input())
S=input()
x=0
ans=0
for i in range(N):
    if S[i]=='I':
        x+=1
    else:
        x-=1
    ans=max(ans,x)
print(ans)
