n=int(input())
l=[int(input()) for i in range(n)]

num=l[0]
cnt=0
for i in range(10**5):
  if num==2:
    cnt+=1
    break
  else:
    num=l[num-1]
    cnt+=1
    
if cnt==10**5:
  cnt=-1
  
print(cnt)
