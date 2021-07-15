from bisect import bisect_left
def check(x):
  cnt=0
  l=n
  r=n
  for i in range(n):
    while True:
      if l==0:
        break
      if a[l-1]<x-a[i]:
        break
      l-=1
    cnt+=(r-l)
  return cnt>=m

n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
ok=0
ng=2*10**5+10
# 幸福度が上位m個に入る最小のAx+Ayを二分探索する。
while abs(ok-ng)>1:
  mid=(ok+ng)//2
  if check(mid):
    ok=mid
  else:
    ng=mid

ru=[0]*(n+1)
for i in range(n):
  ru[i+1]=ru[i]+a[i]

ans=0
cnt=0
r=n
# 幸福度が上位m個に入るAx+Ayの最小値のみm個の個数制限から溢れてしまう場合があるので別に考える
ok=ok+1 # Ax+Ayの最小値より大きな値を先に処理するために最小値+1をする。
for i in range(n):
  # 最小値以外の処理
  l=bisect_left(a,ok-a[i])
  cnt+=r-l
  ans+=(r-l)*a[i]+(ru[r]-ru[l])
ans+=(ok-1)*(m-cnt) # 最小値の処理
print(ans)

