n=int(input())
mod=10**9+7

al=pow(4,n,mod)

import itertools
itr=itertools.product([0,1,2,3],repeat=4)
itr=list(itr)
dic1={} #dec
dic2={} #enc
for i in enumerate(itr):
    dic1[i[0]]=[i[1]]
    dic2[i[1]]=[i[0]]

    

dp=[[0 for i in range(4**3)] for q in range(n+1)]

for i in range(4**3):
    if i!=9 and i!=33 and i!=6:
        dp[3][i]=1


for i in range(3,n):
    for q in range(4**3):
        for r in range(4):
            p1=q//16%4
            p2=q//4%4
            p3=q%4
            
            if p2==0 and p3==2 and r==1:
                continue
            if p1==0 and p3==2 and r==1:
                continue
            if p1==0 and p2==2 and r==1:
                continue
            if p2==0 and p3==1 and r==2:
                continue
            if p2==2 and p3==0 and r==1:
                continue
        
            ck=q%16*4
            dp[i+1][ck+r]+=dp[i][q]
            dp[i+1][ck+r]%=mod

print((sum(dp[n])%mod))
  

