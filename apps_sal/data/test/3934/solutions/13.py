n=int(input())
List=[]
vertecies=[0]*n
for i in range(0,n-1):
  OP=[]
  OP=list(map(int, input().split()))
  List.append(OP)
  vertecies[OP[0]-1]=vertecies[OP[0]-1]+1
  vertecies[OP[1]-1]=vertecies[OP[1]-1]+1
#print(vertecies)
k=0
for i in range (0,n):
  if vertecies[i]==2:
    k=k+1
if k>0:
  print("NO")
else:
  print("YES")
