x=int(input())

num=0
cnt=0

for i in range(1,10**9):
  num+=i
  cnt+=1
  if num>=x:
    break
    
print(cnt)
