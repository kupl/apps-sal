import math

n,m=list(map(int,input().split()))
a=list(map(int,input().split()))

if n==1:
  a1=a[0]//2
  ans_m=m//a1
  if ans_m==0:
    print((0))
  else:
    print(((ans_m-1)//2+1))
  
else:
  x=a[0]
  ch=0
  ch1=0
  while x%2==0:
    x=x//2
    ch+=1
  dob=2**ch
  for i in a:
    if i%dob==0 and i%(dob*2)!=0:
      ch1+=1
  if ch1!=n:
    print((0))
  else:
    ans=a[0]//2
    for j in range(1,n):
      ans=(ans*(a[j]//2))//math.gcd(ans,a[j]//2)
    ans_m=m//ans
    if ans_m==0:
      print((0))
    else:
      print(((ans_m-1)//2+1))
    
      

