a,b=map(str, input().split())
q=0
for i in range(1000):
  if int(a+b)==i**2:
    print('Yes')
    q=1
    break
if q==0:
    print('No')
