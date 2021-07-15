n=list(map(int,input().split()))
a=list(map(int,input().split()))
if n[2]>=n[3]:
  print (n[0]*n[1])
else:
  print (n[0]*n[1]+(n[4]*n[0]-sum(a))*(n[3]-n[2]))
