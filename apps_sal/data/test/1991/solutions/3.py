
T = int(input())


for i in range(T):
  n = int(input())
  #n,m = map(int, input().split())
  #a,b = map(int, input().split())
  a = list(map(int,input().split()))
  #a = list(input())
  if a == sorted(a):
    print(0)
    continue
  
  strt = True
  count = 0
  for i in range(n):
    if strt and i+1 != a[i]:
      strt = False
    if not strt and i+1 == a[i]:
      count+=1
  
  end = True
  for i in range(n-1,-1,-1):
    if end and i+1 == a[i]:
      count-=1
    else:
      break
  
  if count==0:
    print(1)
  else:
    print(2)

