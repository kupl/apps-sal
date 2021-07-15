n=int(input())
a=list(map(int,input().split()))
if 0 in a:
  print(sum(abs(i)for i in a))
else:
  pc=mc=0
  for i in range(n):
    if a[i]>0:pc+=1
    else:mc+=1
    a[i]=abs(a[i])
  if mc%2:print(sum(a)-min(a)*2)
  else:print(sum(a))
