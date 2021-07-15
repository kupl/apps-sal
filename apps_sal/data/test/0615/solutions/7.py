n = int(input())
a = [int(item) for item in input().split()]

cumsum = [0] * n
for i in range(n):
  if i == 0:
    cumsum[0] = a[0]
  else:
    cumsum[i] = cumsum[i-1] + a[i]
    
l = 0
r = 2
ans = sum(a)
for i in range(1, n-1):
  while cumsum[i] - cumsum[l+1] > cumsum[l]:
    l += 1
  while cumsum[-1] - cumsum[r+1] > cumsum[r] - cumsum[i]:
    r += 1
  a = cumsum[l]
  b = cumsum[i] - cumsum[l]
  c = cumsum[r] - cumsum[i]
  d = cumsum[-1] - cumsum[r]
  
  ans = min(ans, max(a,b,c,d) - min(a,b,c,d))
print(ans)
