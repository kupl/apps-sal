from sys import stdin
n,m,k=list(map(int,stdin.readline().strip().split()))
s=tuple(map(int,stdin.readline().strip().split()))
x=0
y=0
ans=0
for i in range(n-1,-1,-1):
    if x==m:
        break
    if y+s[i]>k:
        if s[i]>k:
            break
        x+=1
        if x==m:
            break
        ans+=1
        y=s[i]
    else:
        y+=s[i]
        ans+=1
    
print(ans)

