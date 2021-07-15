n,m,x,y=map(int,input().split())
for i in [i for i in range(max(list(map(int,input().split())))+1,min(list(map(int,input().split())))+1)]:
  if x<i<=y: print('No War');break
else:
  print('War')
