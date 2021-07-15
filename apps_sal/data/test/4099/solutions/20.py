n,k,m = map(int,input().split())
a = list(map(int,input().split()))

p = n*m - sum(a)
if p > k :
  ans = -1
elif p < 0:
  ans = 0
else:
  ans = p

print(ans)
