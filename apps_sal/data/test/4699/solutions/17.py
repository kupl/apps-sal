n,k = list(map(int,input().split()))
if k == 0:
  print(n)
  return
dislike = list(input().split())
 
ans = n-1
flag = 1
while flag == 1:
  ans+=1
  flag = 0
  for i in str(ans):
    if i in dislike:
      flag = 1
      break
print(ans)

