N = int(input())
Alist = list(map(int,input().split()))

num = 0
for i in range(N):
  if Alist[i]%2==0:
    num+=1
    #print (Alist[i])
    if Alist[i]%3==0 or Alist[i]%5==0:
      num-=1
      
if num==0:
  print ('APPROVED')
else :
  print ('DENIED')
