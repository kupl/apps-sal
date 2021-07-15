n=int(input())
s=input()
x=0
y=0
ans=0
for i in range(n-1):
    if s[i]=='U':
        y+=1
    else:
        x+=1
    if y==x and s[i+1]==s[i]:
        ans+=1
print(ans)

