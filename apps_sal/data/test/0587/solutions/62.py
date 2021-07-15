import heapq
N,K = list(map(int, input().split()))

I = []
for _ in range(N):
  t,d = list(map(int, input().split()))
  I.append((d,t))
  
I.sort(reverse=True)

# heap_can_delete
h_d = []
# heap_can_add
h_a = []

wk = 0
kind = 0
# 出現したことのあるネタ
ap = set()
for i in range(K):
  d,t = I[i]
  wk += d
  if t not in ap:
    ap.add(t)
    kind += 1
  else:
    heapq.heappush(h_d, (d,t))

for i in range(K,N):
  d,t = I[i]
  if t not in ap:
    ap.add(t)
    # maxをpopさせるために、価値を-1かけておく
    heapq.heappush(h_a, ((-1) * d, t))
  
ans = wk + kind ** 2
while len(h_d) > 0 and len(h_a) > 0:
  d1,t1 = heapq.heappop(h_d)
  d2,t2 = heapq.heappop(h_a)
  d2 = (-1) * d2
  wk = wk - d1 + d2
  kind += 1
  ans = max(ans, wk + kind ** 2)
  
print(ans)
  

