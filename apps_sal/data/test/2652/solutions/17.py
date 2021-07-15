import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

N=int(input())

xylist,yxlist=[],[]
par_dic={}
for i in range(N):
  x,y=map(int,input().split())
  xylist.append((x,y))
  yxlist.append((y,x))
  par_dic[(x,y)]=(x,y)
xylist.sort()
yxlist.sort()
#print(xylist)

elist=[]
for i in range(1,N):
  x1,y1=xylist[i-1]
  x2,y2=xylist[i]
  elist.append((min(abs(x2-x1),abs(y1-y2)),(x1,y1),(x2,y2)))
  y1,x1=yxlist[i-1]
  y2,x2=yxlist[i]
  elist.append((min(abs(x2-x1),abs(y1-y2)),(x1,y1),(x2,y2)))
#print(hq)
elist.sort(reverse=True)

def get_par(x):
  if x == par_dic[x]:
    return x
  else:
    par_dic[x] = get_par(par_dic[x])
    return par_dic[x]
def merge(x,y):
  par_x = get_par(x)
  par_y = get_par(y)
  if par_x != par_y:
    par_dic[par_y] = par_x
def is_same(x,y):
  return get_par(x) == get_par(y)

answer=0
while elist:
  d,p1,p2=elist.pop()
  #print(d,p1,p2)
  if not is_same(p1,p2):
    merge(p1,p2)
    answer+=d
  
print(answer)
