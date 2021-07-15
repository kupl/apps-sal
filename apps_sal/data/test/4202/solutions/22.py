l,r = list(map(int,input().split()))
MOD = 2019
ans = MOD

if r-l+1>=MOD:
    kouho=list(range(MOD))
else:
    kouho=[i%MOD for i in list(range(l,r+1))]
    
for i in range(len(kouho)):
    for j in range(i+1,len(kouho)):
        ans=min(ans,(kouho[i]*kouho[j])%MOD)

print(ans)

