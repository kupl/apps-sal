n, l = list(map(int, input().split()))
s = n*(l-1) + n*(n+1)/2
c = abs(s)
j = 1
for i in range(n):
  t = s - (l+i)
  T = abs(s-t)
  if T < c:
    c = T
    j = i
ans = s -(l+j)
print((int(ans)))


