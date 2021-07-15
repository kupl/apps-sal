from heapq import *
MAX=2*10**5+1

N,Q=list(map(int,input().split()))

I=[[] for _ in range(N+1)]
P=[[[],[]] for _ in range(MAX)]
S=[[],[]]

def heapdel(l,a):
  if l[0][0]==a:
    heappop(l[0])
    while l[1] and l[1][0]==l[0][0]:
      heappop(l[1])
      heappop(l[0])
  else:
    heappush(l[1],a)

def heapadd(l,a):
  heappush(l[0],a)

def heapmin(l):
  return l[0][0]

def main():
  for i in range(1,N+1):
    a,b=list(map(int,input().split()))
    I[i]+=[a,b]
    heapadd(P[b],-a)

  for i in range(1,MAX):
    if P[i][0]:
      heapadd(S,-heapmin(P[i]))

  for i in range(Q):
    c,d=list(map(int,input().split()))
    a,b=I[c]

    heapdel(S,-heapmin(P[b]))
    heapdel(P[b],-a)
    if P[b][0]:
      heapadd(S,-heapmin(P[b]))

    if P[d][0]:
      heapdel(S,-heapmin(P[d]))
    heapadd(P[d],-a)
    heapadd(S,-heapmin(P[d]))

    I[c][1]=d
    print((heapmin(S)))

main()

