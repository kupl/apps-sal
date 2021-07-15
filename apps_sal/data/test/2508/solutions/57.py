def main():
  import sys
  input=sys.stdin.readline
  h,w,k=map(int,input().split())
  sx,sy,tx,ty=map(int,input().split())
  b=[[-1]*(w+2)]
  for i in range(h):
    s=input()
    bb=[-1]
    for j in s:
      if j==".":bb.append(0)
      else:bb.append(-1)
    bb.append(-1)
    b.append(bb)
  b.append([-1]*(w+2))
  d=[]
  d.append((sx,sy))
  for ss in d:
    x,y=ss
    if x==tx and y==ty:
      print(b[x][y]);return
    for i in range(1,k+1):
      if b[x+i][y]<=b[x][y] and b[x+i][y]!=0:break
      if b[x+i][y]==0:d.append((x+i,y))
      b[x+i][y]=b[x][y]+1
    for i in range(1,k+1):
      if b[x-i][y]<=b[x][y] and b[x-i][y]!=0:break
      if b[x-i][y]==0:d.append((x-i,y))
      b[x-i][y]=b[x][y]+1
    for j in range(1,k+1):
      if b[x][y+j]<=b[x][y] and b[x][y+j]!=0:break
      if b[x][y+j]==0:d.append((x,y+j))
      b[x][y+j]=b[x][y]+1
    for j in range(1,k+1):
      if b[x][y-j]<=b[x][y] and b[x][y-j]!=0:break
      if b[x][y-j]==0:d.append((x,y-j))
      b[x][y-j]=b[x][y]+1
  print(-1)
def __starting_point():
  main()

__starting_point()
