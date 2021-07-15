from collections import deque
N,Q = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(N-1)]
px = [list(map(int,input().split())) for _ in range(Q)]

tree = [[] for _ in range(N)]
for a, b in ab:
  tree[a-1].append(b-1)
  tree[b-1].append(a-1)

counter = [0] * N
for p, x in px:
  counter[p-1] += x
  
flag = [1] * N
t = deque()
t.append(0)

#1(0)から順に探索していけば、自然と親→子の順番になる
while t:
  v = t.popleft()
  flag[v] = 0
  for i in tree[v]:
    if flag[i]:
      counter[i] += counter[v]
      t.append(i)
      
print(*counter)
