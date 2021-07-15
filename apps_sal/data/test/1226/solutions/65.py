#powは繰り返し2乗法により指数計算を行う関数
mod=10**9+7
n,a,b=list(map(int,input().split()))

ans=pow(2,n,mod)-1 #n種類の花を使って花束を作る総数は2^n-1通り

comb1=1 #nCaの計算
for i in range(n-a+1,n+1): #n*(n-1)*…*(n-a+1)を計算
    comb1*=i
    comb1%=mod
for i in range(1,a+1): #1/a!=1/(1*2*…*a)=1^(p-2)*2^(p-2)*…*a^(p-2) (p=10**9+7)を計算
    comb1*=pow(i,mod-2,mod) # iの逆元 →　1/iした際に かける(iの逆元)とすればあまりが求まる
    comb1%=mod

comb2=1
for i in range(n-b+1,n+1): #n*(n-1)*…*(n-b+1)を計算
    comb2*=i
    comb2%=mod
for i in range(1,b+1): #1/b!=1/(1*2*…*b)=1^(p-2)*2^(p-2)*…*b^(p-2) (p=10**9+7)を計算
    comb2*=pow(i,mod-2,mod)
    comb2%=mod

ans-=(comb1+comb2) #nCa、nCbを総数から引く
ans%=mod
print(ans)

