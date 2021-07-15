x, k, d=map(int,input().split())
x=abs(x)
#k回すべて戻っても0に達せない場合  k-x//d
if x//d>=k:
  print(x-k*d)
elif (k-x//d)%2==0:
  print(x%d)
else:
  print(abs(x-x//d*d-d))
