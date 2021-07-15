from collections import Counter, deque
def lInt(d = None): return map(int, input().split(d))

n, m, k, *_ = lInt()
a = list(lInt())
f = [0]*1000002
d = deque()
acc = 0; ans = 0

for v in a:
  f[v] = 1
for i in range(1, m+1):
  if f[i]:
    acc += f[i]
    d.append(i)
for i in range(m+1, 1000002):
  while acc >= k:
    j = d.pop()

    if f[j]:
      f[j] = 0
      ans += 1
      acc -= 1

  if f[i]:
    acc += f[i]
    d.append(i)
  if f[i-m]:
    acc -= 1
print(ans)
