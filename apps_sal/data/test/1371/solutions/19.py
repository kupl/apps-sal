S=int(input())
ans=[0]*(S+1)
MOD=10**9+7

if S<=2:
    print(0)
    return
elif S==3:
    print(1)
    return   
ans[3]=1
for i in range(4,S+1):
    ans[i]=ans[i-1]+ans[i-3]

print(ans[i]%MOD)
