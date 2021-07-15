N, X, M = map(int, input().split())

li = [-1 for i in range(M)]
a = []
l = 0
tot = 0
while li[X]==-1:
  a.append(X)
  li[X] = l
  l += 1
  tot += X
  X = (X*X)%M

c = l - li[X]
s = 0
for i in range(li[X],l):
  s += a[i]

ans = 0
if N<=l:
  for i in range(N):
    ans += a[i]
else:
  ans += tot
  N -= l
  ans += s*int(N/c)
  for i in range(N%c):
    ans += a[li[X]+i]
print(ans)
