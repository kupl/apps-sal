from collections import deque

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

que = deque([[i] for i in range(1, N+1)])
lst = []

while que:
  seq = que.popleft()
  if len(seq) == N:
    lst.append(seq)
  else:
    for j in range(1, N+1):
      if j not in seq:
        que.append(seq + [j])

print(abs(lst.index(P) - lst.index(Q)))
