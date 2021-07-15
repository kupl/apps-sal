N,Z,W=map(int,input().split())
alist=list(map(int,input().split()))

if N==1:
  print(abs(alist[-1]-W))
else:
  ans1=abs(alist[-2]-alist[-1])
  ans2=abs(alist[-1]-W)
  print(max(ans1,ans2))
