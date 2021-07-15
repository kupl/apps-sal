from heapq import heapify, heappop, heappush

N = int(input())
A = list(map(int, input().split()))
A = [-a for a in A]

L = [[a, i] for i, a in enumerate(A[:2*N])]
Sl = 0
heapify(L)
used = set()
for i in range(N):
  a, i = heappop(L)
  used.add(i)
  Sl -= a

R = A[2*N:].copy()
Sr = -sum(R)
heapify(R)

ans = Sl - Sr
for i in range(2*N-1, N-1, -1):
  a = - A[i]
  r =  - heappop(R)
  if a > r:
    heappush(R, -r)
  else:
    Sr += a - r
    heappush(R, -a)
  if i in used:
    while L:
      l, j = heappop(L)
      l *= -1
      if j < i:
        Sl += l - a
        used.add(j)
        break
  ans = max(ans, Sl - Sr)

print(ans)
