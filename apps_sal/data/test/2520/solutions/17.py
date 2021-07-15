N, M, K = list(map(int, input().split()))
friend = [[] for _ in range(N+1)]
block = [[] for _ in range(N+1)]

for i in range(M):
  A,B = list(map(int, input().split()))
  friend[A].append(B)
  friend[B].append(A)

for i in range(K):
  C,D = list(map(int, input().split()))
  block[C].append(D)
  block[D].append(C)
#print(friend)
#print(block)

#import queue
grouping = [False]*(N+1)
#print(grouping)
grouping[0] = True
group = [0]*(N+1)
g_num = 0
g_cnt = []
for i in range(1,N+1):
  cnt = 0
  if grouping[i] == True:
    continue 
  group[i] = g_num
  grouping[i] = True
  #q = queue.Queue()
  #q.put(i)
  stack = [i]
  #while not q.empty():
  while len(stack)>0:
    #print('v:',visited)
    #p = q.get()
    p = stack.pop()
    for f in friend[p]:
      #print(p,f)
      if grouping[f]==False:
        #q.put(f)
        stack.append(f)
        group[f]=g_num
        grouping[f] =True
        cnt += 1
  g_num += 1
  g_cnt.append(cnt)
  #print('g:',grouping)
ans = []
for i in range(1,N+1):
  c = g_cnt[group[i]]-len(friend[i])
  for b in block[i]:
    if group[b]==group[i]:
      c -= 1
  ans.append(c)
print((*ans))

