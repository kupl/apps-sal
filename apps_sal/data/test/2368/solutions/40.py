import queue
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
nds = [[] for _ in range(N)]
vstd = [False for _ in range(N)]
ans = "Yes"
for i in range(M):
  c,d = map(int,input().split())
  c -= 1
  d -= 1
  nds[c].append(d)
  nds[d].append(c)
for i in range(N):
  if vstd[i]:
    continue
  q = queue.Queue()
  q.put(i)
  vstd[i] = True
  
  a = 0
  b = 0
  while not q.empty():
    idx = q.get()
    a += A[idx]
    b += B[idx]
    for e in nds[idx]:
      if vstd[e]:
        continue
      vstd[e] = True
      q.put(e)
  if a!=b:
    ans = "No"
print(ans)
