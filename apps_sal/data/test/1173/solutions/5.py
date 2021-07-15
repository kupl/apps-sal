from collections import deque

def main():
  n=int(input())
  a=[0]*n
  for i in range(n):
    a[i]=deque(list(map(lambda x:int(x)-1,input().split())))
  q=deque([])
  tmp=set()
  for idx,i in enumerate(a):
    x=idx
    y=i[0]
    if x == a[y][0]:
      tmp.add(x)
      tmp.add(y)
  q=deque(tmp)
  for i in tmp:
    a[i].popleft()
  
  
  day=0
  while True:
    day+=1
    t=q.copy()
    q=deque()
    tmp=set()
    while t:
      x=t.popleft()
      if len(a[x])==0: continue;
      y=a[x][0]
      if x == a[y][0]:
        tmp.add(x)
        tmp.add(y)
    q=deque(tmp)
    for i in tmp:
      a[i].popleft()
    if len(q)==0: break;

  for i in range(n):
    if len(a[i])!=0:
      print(-1)
      return
  print(day)


def __starting_point():
  main()
__starting_point()
