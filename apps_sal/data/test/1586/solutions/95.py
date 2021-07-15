#まずnが奇数なら値は0
#nが偶数なら素因数5の個数
#素因数10の個数を求めたい
n=int(input())
if n%2==1:
  print((0))
else:
  ans=0
  num=5
  n=n//2
  while num<=n:
    ans+=n//num
    num=num*5
  print(ans)

