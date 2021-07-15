import collections, heapq

def dijkstra(g, st):
    """Dijkstra method"""

    n = len(g)
    d = [float('inf')] * n
    d[st] = 0

    que = [(0, st)]     # (min_dist, vertex)
    heapq.heapify(que)

    while len(que) > 0:
        dist, v0 = heapq.heappop(que)
        if d[v0] < dist: continue
        for v1, dist in g[v0]:
            if d[v1] > d[v0] + dist:
                d[v1] = d[v0] + dist
                heapq.heappush(que, (d[v1], v1))

    return d

n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]

d = collections.defaultdict(list)

for pi in p:
  d[max(pi[0],pi[1])].append(pi)

levels = list(d.keys())
levels.sort()

g = [[] for _ in range(2*(len(levels)+1))]

ans = 0
last = [(0,0)]
for k, l in enumerate(levels):
  d[l].sort(key=lambda x: (x[0], -x[1]))
  if d[l][0][0] == d[l][-1][0]:
    ans += d[l][0][1] - d[l][-1][1] 
  elif d[l][0][1] == d[l][-1][1]:
    ans += d[l][-1][0] - d[l][0][0]
  else:
    ans += (l-d[l][0][0]) + (l-d[l][-1][1])
  
  cand = [d[l][0]]
  if len(d[l]) > 1:
    cand.append(d[l][-1])
    
  for i, vi in enumerate(last):
    for j, vj in enumerate(cand):
      dist = abs(last[i-1][0]-vj[0]) + abs(last[i-1][1]-vj[1])
      g[2*k+i].append((2*k+2+j, dist))
      g[2*k+2+j].append((2*k+i, dist))

  last = cand

# print(g)
res = dijkstra(g, 0)
print(ans+min(res[-2:]))

