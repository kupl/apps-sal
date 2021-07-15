N,K=list(map(int,input().split()))
S=input()
flag=False
cnt=[]
l=0
r=0
cnt.append([0,0])
for i in range(N):
    if flag:
        if S[i]=='0':
            r=i
            cnt.append([l,r])
            flag=False
    else:
        if S[i]=='1':
            l=i
            flag=True
if flag:
    cnt.append([l,N])
cnt.append([N,N])
ans=0
n=len(cnt)
for i in range(n):
    j=min(n-1,i+K)
    ans=max(cnt[j][1]-cnt[i][0],ans)
print(ans)

