from heapq import *
N,M = map(int,input().split())
L = [[] for m in range(M)]
H = []
ans = 0

for n in range(N):
  a,b = map(int,input().split())
  if a<=M:
    L[M-a]+=[b]
    
for m in range(M-1,-1,-1):
  for l in L[m][::-1]:
    heappush(H,-l)
  if 0<len(H):
    ans-=heappop(H)

print(ans)
