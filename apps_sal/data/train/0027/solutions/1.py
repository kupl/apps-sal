t=int(input())
for g in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  b=list()
  for i in range(n):
    while a[i]%2==0:
      b.append(a[i])
      a[i]=a[i]//2
  b.sort()
  count=1
  for i in range(len(b)-1):
    if b[i]!=b[i+1]:
      count+=1
  if len(b)==0:
    print(0)
  else:
    print(count)

