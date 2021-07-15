N,T=map(int,input().split())
li=[list(map(int,input().split())) for i in range(N)]
li2=[]
for i in range(N):
  if li[i][1]<=T:
    li2.append(li[i])
li2.sort()
if len(li2)==0:
  print('TLE')
  return
print(li2[0][0])
