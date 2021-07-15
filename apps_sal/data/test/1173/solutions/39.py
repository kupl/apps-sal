N=int(input())
a=[[0 for j in range(N-1)] for i in range(N)]
for i in range(N):
  line=list(map(int,input().split()))
  for j in range(N-1):
    a[i][j]=line[j]-1
  a[i]=a[i][::-1]
    
stack=[]

def addmatch(i):
  if len(a[i])==0:
    return
  j=a[i][-1]
  if a[j][-1]==i:
    stack.append([i,j])

for i in range(N):
  addmatch(i)

day=0
while stack:
  day+=1
  member=set()
  for i in range(len(stack)):
    g=stack.pop()
    y=g[0]
    x=g[1]
    if len(a[y])>0 and a[y][-1]==x:
      a[y].pop()
      a[x].pop()
      member.add(y)
      member.add(x)
  for m in member:
    addmatch(m)

for i in range(len(a)):
  if len(a[i])>0:
    print(-1)
    break
else:
  print(day)
