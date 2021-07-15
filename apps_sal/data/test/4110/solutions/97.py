D,G=list(map(int,input().split()))
p=list()
c=list()
for _ in range(D):
  P,C=list(map(int,input().split()))
  p.append(P)
  c.append(C)
ans=1<<29
for bit in range(1<<D):
  sum_=0
  num_=0
  for i in range(D):
    if bit&(1<<i):
      sum_+=c[i]+p[i]*100*(i+1)
      num_+=p[i]
  if sum_>=G:
    ans=min(ans,num_);
  else:
    for i in range(D-1,-1,-1):
      if bit&(1<<i):
        continue
      for j in range(p[i]):
        if sum_>=G:
          break
        sum_+=100*(i+1)
        num_+=1
    ans=min(ans,num_);
print(ans)

