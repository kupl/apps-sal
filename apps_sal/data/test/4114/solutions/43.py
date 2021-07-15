N=int(input())
L=[list(map(int,input().split())) for i in range(N)]
L.sort(key=lambda x:x[2],reverse=True)
for i in range(101):
  for j in range(101):
    s=L[0][2]+abs(i-L[0][0])+abs(j-L[0][1])
    for l in L[1:]:
      h=l[2]+abs(i-l[0])+abs(j-l[1])
      if s==h:
        continue
      elif l[2]==0 and s<h:
        continue
      else:
        break
    else:
      print(i,j,s)
      return
