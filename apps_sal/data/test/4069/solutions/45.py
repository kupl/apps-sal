# まず極力原点に近づく。
# 原点を超えた場合は、切り返す
# シミュレートは遅いので、短絡させる。

x,k,d=list(map(int,input().split()))
absx=abs(x)
step1= absx // d
if step1 >= k:
  print((absx-(d*k)))
else:
  step2=k-step1
  absx-=(d*step1)
  if step2 % 2==0:
    print(absx)
  else:
    print((abs(absx-d)))

