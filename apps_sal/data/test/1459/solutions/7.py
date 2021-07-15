n=int(input())

s=(input().split())
for i in range(n):
    s[i]=int(s[i])

a,b=list(map(int,input().split()))

if(a>b):
    t=a
    a=b
    b=t
s1=s[a-1:b-1]
s2=s[b-1:]+s[:a-1]
ans1=0
ans2=0
for item in s1:
    ans1+=item

for item in s2:
    ans2+=item

print(min(ans1,ans2))
    

