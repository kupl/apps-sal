n=int(input())
lx=[]
ly=[]
for i in range(n):
  x,y=map(int,input().split())
  lx.append(x+y)
  ly.append(x-y)
print(max(max(lx)-min(lx),max(ly)-min(ly)))
