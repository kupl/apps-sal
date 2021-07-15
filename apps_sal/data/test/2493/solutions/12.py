def comb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル
n=int(input())
mod=10**9+7
for i in range( 2, n + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
import copy
a=list(map(int,input().split()))
b=copy.deepcopy(a)
b.sort()
tmp=-1
for i in range(n):
  if b[i]==b[i+1]:
    tmp=b[i]
r=[]
for i in range(n+1):
  if a[i]==tmp:
    r.append(i)
y=abs(r[1]-r[0]-1)
for k in range(1,n+2):
  ans=(comb(n-1,k,mod)+comb(n-1,k-2,mod)+comb(n-1,k-1,mod)*2-comb(n-1-y,k-1,mod))%mod
  print(ans)
