from collections import deque
n = int(input())
a = [[] for i in range(n)]
e = []
for i in range(n-1):
  b, c = map(int, input().split())
  b -= 1
  c -= 1
  a[b].append(c)
  e.append(c)
col = [0 for i in range(n)]
v = deque([0])

while v:
  d = v.popleft()
  k = 1
  for i in a[d]:
    if col[d] == k:
      k += 1
    col[i] = k
    v.append(i)
    k += 1
print (max(col))
for i in e:
  print(col[i])
