n,d=map(int,input().split())
if n%(2*d+1)==0:
  print(n//(2*d+1))
else:
  print(n//(2*d+1)+1)
