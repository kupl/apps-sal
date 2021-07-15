N=int(input())
S=input()
x=0
ans=0
for c in S:
    if c=='I':
        x+=1
        ans=max(ans,x)
    else:
        x-=1
print(ans)

