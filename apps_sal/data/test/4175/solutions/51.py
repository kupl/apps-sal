n=int(input())
w=[]
for i in range(n):
  w.append(input())
ans=True
for i in range(n-1):
  if w[i][-1]!=w[i+1][0]:
    ans=False
if len(set(w))!=n:
  ans=False
if ans:
  print('Yes')
else:
  print('No')
