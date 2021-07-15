n,m=list(map(int,input().split()))
mod=pow(10,9)+7
# n<=m
# コンビネーション、さらに高速。あらかじめO(N)の計算をすることでのちの計算が早くなる
def cmb(n,r,mod):
  if (r<0 or r>n):
    return 0
  r=min(r,n-r)
  return g1[n]*g2[r]*g2[n-r]%mod
g1=[1,1] # g1[i]=i! % mod
g2=[1,1] # g2[i]=(i!)^(-1) % mod
inverse=[0,1]
for i in range(2,m+1):
  g1.append((g1[-1]*i)%mod)
  inverse.append((-inverse[mod%i]*(mod//i))%mod)
  g2.append((g2[-1]*inverse[-1])%mod)

# 数列aの作り方
ans_a=g1[m]*g2[m-n]

# 数列bの作り方
ans_b=0
for i in range(n+1):
  tmp=cmb(n,i,mod)
  tmp*=(g1[m-i]*g2[m-n])%mod
  tmp%=mod
  ans_b+=tmp*(-1)**i
  ans_b%=mod
  #print(i,tmp,ans_b)

print(((ans_a*ans_b)%mod))
#print(ans_a,ans_b)


