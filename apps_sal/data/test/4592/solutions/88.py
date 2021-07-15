N=int(input())
table=[True for _ in range(N+1)]
table[0]=False
table[1]=False
for i in range(2,N+1):
    if table[i]==False:
        continue
    for j in range(2,N//i):
        table[i*j]=False
p=[]
for i in range(N+1):
    if table[i]:
        p.append(i)

n=len(p)
cnt=[0 for _ in range(n)]
for i in range(2,N+1):
    x=i
    j=0
    while x>1:
        while x%p[j]==0:
            cnt[j]+=1
            x//=p[j]
        j+=1
ans=1
MOD=1000000007
for i in range(n):
    ans*=cnt[i]+1
    ans%=MOD
print(ans)

