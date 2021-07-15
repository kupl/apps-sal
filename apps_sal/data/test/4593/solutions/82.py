x=int(input())
ans=0
if x==1:
  print(1)
  return
for i in range(1,x):
  for j in range(2,10):
    if i**j<=x:
      ans=max(ans,i**j)
    else:
      break
print(ans)
