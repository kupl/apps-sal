n,W=map(int,input().split())
w=[0]*n
v=[0]*n
for i in range(n):
  w[i],v[i]=map(int,input().split())
ws=w[0]
V=[[] for i in range(4)]
for i in range(n):
  V[w[i]-ws].append(v[i])
V[0].sort(reverse=True)
V[1].sort(reverse=True)
V[2].sort(reverse=True)
V[3].sort(reverse=True)
VV=[[0] for i in range(4)]
for i in range(4):
  for j in range(len(V[i])):
    VV[i].append(VV[i][-1]+V[i][j])
ans=0
for i in range(len(V[0])+1):
  for j in range(len(V[1])+1):
    for k in range(len(V[2])+1):
      for l in range(len(V[3])+1):
        if i*ws+j*(ws+1)+k*(ws+2)+l*(ws+3)>W:
          break
        if VV[0][i]+VV[1][j]+VV[2][k]+VV[3][l]>ans:
          ans=VV[0][i]+VV[1][j]+VV[2][k]+VV[3][l]
print(ans)
