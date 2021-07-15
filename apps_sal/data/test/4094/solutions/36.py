k=int(input())
a=0
cnt=-1
for i in range(1,k+1):
  a=(10*a+7)%k
  if a==0:
    cnt=i
    break
print(cnt)
