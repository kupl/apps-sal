t=int(input())
for _ in range(t):
 n,b=list(map(int,input().split()))
 low=0
 high=n
 while low<high:
  mid=(low+high)//2
  cook=mid
  left=mid
  while True:
   book=left//b
   if book==0:
    break
   left=book+left%b
   cook+=book
  #  print(low,high,mid,cook)
  if high-low<3:
   for i in range(low,high+1):
    cook=i
    left=i
    while True:
     book=left//b
     if book==0:
      break
     left=book+left%b
     cook+=book
    ans=i
    if cook>=n:
     break
   break
  if cook>n:
   ans=mid
   high=mid
  elif cook<n:
   low=mid
  if cook==n:
   ans=mid
   high=mid
 print(ans)
   

