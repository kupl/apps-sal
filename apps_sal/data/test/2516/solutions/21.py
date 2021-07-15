n,p=list(map(int,input().split()))
S=input()[::-1]
ans=0
if p==2:
    for i,s in enumerate(S):
        if int(s)%2==0:
            ans+=(n-i)
    print(ans)
    return

if p==5:
    for i,s in enumerate(S):
        if int(s)==0 or int(s)==5:
            ans+=(n-i)
    print(ans)
    return


sd=0
d=1
count=[0]*(p+1)
count[0]+=1
for s in S:
    sd+=int(s)*d
    d*=10
    sd%=p
    d%=p
    count[sd]+=1

for cnt in count:
    ans+=cnt*(cnt-1)//2

print(ans)


