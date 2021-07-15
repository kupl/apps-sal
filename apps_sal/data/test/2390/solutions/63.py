from heapq import heappush, heappop
N, C, *L = map(int, open(0).read().split())
hq1 = []
hq2 = []
sushi = []
for x,y in zip(*[iter(L)]*2):
  sushi += [(x,y)]
sushi.sort()
x = 0
y = 0
for i in range(N-1,-1,-1):
  p,q = sushi[i]
  x += q
  heappush(hq1,(-x+(C-p),i))
  p,q = sushi[N-1-i]
  y += q
  heappush(hq2,(-y+p,N-1-i))
m = 0
ans1 = 0
for i in range(N):
  x,y = sushi[i]
  m += y
  n = m-x
  while hq1 and hq1[0][1]<=i:
    heappop(hq1)
  if hq1 and hq1[0][0]<-x:
    ans1 = max(ans1, n-hq1[0][0]-x)
  else:
    ans1 = max(ans1,n)
    

m = 0
ans2 = 0
for i in range(N-1,-1,-1):
  x,y = sushi[i]
  m += y
  n = m-(C-x)
  while hq2 and hq2[0][1]>=i:
    heappop(hq2)
  if hq2 and hq2[0][0]<-(C-x):
    ans2 = max(ans2, n-hq2[0][0]-(C-x))
  else:
    ans2 = max(ans2, n)
print(max(ans1,ans2))
