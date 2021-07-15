n = int(input())
l = [0 for _ in range(n)]
already = set()
next = 1
c = 0
for i in range(n):
  a = int(input())
  l[i] = a
while c <= n:
  next = l[next-1]
  c += 1
  if next == 2:
    print(c)
    break
  elif next in already:
    print(-1)
    break
  already.add(next)
