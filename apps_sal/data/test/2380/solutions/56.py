n,m = map(int,input().split())

A = list(map(int,input().split()))

l = []

for i in range(m):
  b,c = map(int,input().split())
  l.append([c,b])

l.sort()
l = l[::-1]

L = []
cn = 0
for b,c in l:
  # print(b,c)
  if cn > n:break
  c = min(c,10**5+10)
  L += [b]*c
  cn += c

L += A

L.sort()
L = L[::-1]
# print(L)
print(sum(L[:n]))
