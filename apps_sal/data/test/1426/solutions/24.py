import sys
input = sys.stdin.readline
def MI():
  return map(int,input().split())
def main():
  n,m=MI()
  G=[[] for _ in range(n)]
  for _ in range(m):
    u,v=MI()
    u-=1
    v-=1
    G[u].append(v)
  s,t=MI()
  s-=1
  t-=1
  
  fi=[True]*n
  se=[True]*n
  th=[True]*n
  th[s]=False

  dq=[s]
  depth=0
  
  while dq:
    depth+=1
    tank1=[]
    tank2=[]
    tank3=[]
    
    for p in dq:
      for c in G[p]:
        if fi[c]:
          fi[c]=False
          tank2.append(c)
    for p in tank2:
      for c in G[p]:
        if se[c]:
          se[c]=False
          tank3.append(c)
    for p in tank3:
      for c in G[p]:
        if th[c]:
          th[c]=False
          tank1.append(c)
        if c==t:
          print(depth)
          return
    dq=tank1
  print(-1)  
def __starting_point():
  main()
__starting_point()
