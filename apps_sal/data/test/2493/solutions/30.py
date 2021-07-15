"""
被りなし
cmb(n-2,k)
被りあり2子使うなら
  x,x,x, A, y,y,y,y, A, z,z,z
cmb(n-2,k-2)
被りあり、１つだけ使うなら。。。
  cmb(n-2,k-1) * 2 # y使うかもしれないけーす
  cmb(count(x) + count(z), k-1) # y使わないケース（２倍カウントしてる）
"""
N = int(input())
A = list(map(int, input().split()))
dup = sum(A) - N*(N+1)//2
idx = []
for i in range(len(A)):
  if A[i] == dup:
    idx.append(i)
    
countXZ = N - idx[1] + idx[0]
### nCr mod
# https://qiita.com/derodero24/items/91b6468e66923a87f39f
mod = 10**9+7 #出力の制限
NMAX = 10**5+10
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NMAX + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

def cmb(n, r, m=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % m

# solve
print(N) # k=1
for k in range(2,N+1):
  wk = cmb(N-1,k)
  wk += cmb(N-1,k-2)
  wk += cmb(N-1,k-1) * 2
  wk -= cmb(countXZ, k-1)
  #print(cmb(N-1,k), cmb(N-1,k-2), cmb(N-1,k-1) * 2, cmb(countXZ, k-1))
  print(wk % mod)
print(1) # k=N+1
