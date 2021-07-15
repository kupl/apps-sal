n,k=map(int,input().split())
a=list(map(int,input().split()))
d={j:0 for j in range(41)}
for ai in a:
  for j in range(41):
    if (ai>>j) & 1:
      d[j]+=1
ans=0
l=len(bin(k))-3
import sys
sys.setrecursionlimit(10**7)

def dp(m,t): # 一番左の桁（l桁目）から考える。一番右の桁は0桁目。t:kより真に小さいかどうか
  if m<0:return 0
  ret=0
  if t==1: # 以降は好きに選んでいいので、最適な数字を選ぶ。一意。
    for i in range(m+1):
      tmp=max(0,n-2*d[i])
      ret+=pow(2,i)*tmp
  else:
    if (k>>m)&1: #kのm桁目が1なら1か0を選べる
      # 1にするとき
      tmp1=dp(m-1,0)+(n-2*d[m])*pow(2,m)
      # 0にするとき
      tmp0=dp(m-1,1)                    
      ret+=max(tmp1,tmp0)
    else:
      ret+=dp(m-1,0)
  return ret

print(sum(a)+dp(l,0))
