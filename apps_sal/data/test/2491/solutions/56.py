from collections import deque
def belman(s,n,w,es):
    d = [-float("inf")] * n #d[i] : s→iの最短距離
    d[s] = 0
    c = 0
    while True:
      update = False
      for p,q,r in es:
        if d[p] != -float("inf") and d[q] < d[p] + r:
          d[q] = d[p] + r
          update = True
          c += 1
        if c > w:
          return 'inf'
      if not update:
        break
    return d[n-1]

def use_path(n,start,es):
    q = deque()
    chk = [False] * n
    q.append(start)
    chk[start] = True
    used = {start}
    while len(q) > 0:
        node = q.popleft()
        for nex in es[node]:
            if not chk[nex]:
                chk[nex] = True
                q.append(nex)
                used.add(nex)
    return used

n,w = map(int,input().split())
es = []
l = [[] for i in range(n)]
r = [[] for i in range(n)]

for i in range(w):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    l[a].append(b)
    r[b].append(a)
    es.append((a,b,c))

use = use_path(n,0,l) & use_path(n,n-1,r)
ess = [(a,b,c) for a,b,c in es if a in use and b in use]
print(belman(0,n,w*2,ess))
