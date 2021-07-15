def beki(a,b):
    waru=10**9+7
    ans=1
    while(b>0):
        if(1 & b):
            ans= ans * a %waru
        b >>= 1
        a=a * a % waru
    return ans

n,m=map(int,input().split())
s=input()


ans=[]
waru=10**9+7
ruiseki=[0]*(n+1)
bekij=[1]*(n+1)
for i in range(n):
    ruiseki[i+1]=ruiseki[i]+int(s[i])
    bekij[i+1]=(bekij[i]*2)%waru
for i in range(m):
    l,r=map(int,input().split())
    ko=ruiseki[r]-ruiseki[l-1]
    ans.append(str((((bekij[ko] -1)) * ((bekij[r+1-l - ko]))) %waru))

print("\n".join(ans))
