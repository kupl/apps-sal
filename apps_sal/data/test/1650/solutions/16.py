L=str(input())
ls=len(L)
cnt=0
ans=0
MOD=10**9+7
for i in range(ls):
    if L[i]=="1":
        tmp=pow(3,ls-(i+1),MOD)*pow(2,cnt,MOD)
        tmp%=MOD
        ans+=tmp
        cnt+=1
ans+=pow(2,cnt,MOD)
print(ans%MOD)
