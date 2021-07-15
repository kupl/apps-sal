import sys
sys.setrecursionlimit(10**5)

def f(x):
  for tmp in links[x]:
    if c[tmp[0]]<0:
      if tmp[1]%2==0:
        c[tmp[0]]=c[x]+0
      else:
        c[tmp[0]]=1-c[x]
      f(tmp[0])

N=int(input())
links=[[] for _ in range(N+1)]
for _ in range(N-1):
  u, v, w=map(int, input().split())
  links[u].append([v, w])
  links[v].append([u, w])
  
c=[-1]*(N+1)
c[1]=0
f(1)

print(*c[1:], sep='\n')
