n=int(input())
p=list(map(int,input().split()))
s=input()
maxi=0
temp=0
local=-1
for i in range(n):
    if s[i]=='A':
        temp+=p[i]
    else:
        temp-=p[i]
    if temp>maxi:
        local=i
        maxi=temp
ans=0

for i in range(local+1):
    if s[i]=='A':
        ans+=p[i]


for i in range(local+1,n):
    if s[i]=='B':
        ans+=p[i]

maxi=0
temp=0
local=-1
p=list(reversed(p))
s=s[::-1]
for i in range(n):
    if s[i]=='A':
        temp+=p[i]
    else:
        temp-=p[i]
    if temp>maxi:
        local=i
        maxi=temp
ans1=0
for i in range(local+1):
    if s[i]=='A':
        ans1+=p[i]
for i in range(local+1,n):
    if s[i]=='B':
        ans1+=p[i]

print(max(ans,ans1))

