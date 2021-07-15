import heapq

n = int(input())
a = list(map(int, input().split()))
plus = [sum(a[:n])]
minus = [-sum(a[-n:])]
p = a[:n]
m = [-i for i in a[-n:]]
heapq.heapify(p)
heapq.heapify(m)
for i in range(n,2*n):
  pn = a[i]
  mn = -a[-(i+1)]
  if pn > p[0]:
    plus.append(plus[-1] + pn - heapq.heappop(p))
    heapq.heappush(p, pn)
  else:
    plus.append(plus[-1])
  if mn > m[0]:
    minus.append(minus[-1] + mn - heapq.heappop(m))
    heapq.heappush(m, mn)
  else:
    minus.append(minus[-1])
minus.reverse()
ans = []
for i,j in zip(plus,minus):
  ans.append(i+j)
print(max(ans))
