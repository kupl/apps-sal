n,m=map(int,input().split())
data=[0]*n
for i in range(m):
  a,b=map(int,input().split())
  if a==1:
    data[b-1]+=1
    if data[b-1]==2:
      print('POSSIBLE')
      return
  if b==n:
    data[a-1]+=1
    if data[a-1]==2:
      print('POSSIBLE')
      return

print('IMPOSSIBLE')
