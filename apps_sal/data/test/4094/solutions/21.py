k=int(input())
a=0
c=0
t=1
for i in range(k):
  a=(a*10+7)%k
  c+=1
  if a==0:
    t=0
    print(c)
    break
if t:
  print((-1))

