n,k,t = list(map(int, input().split()))
if t < k:
  print(t)
elif t > n:
  print(max(0, k-t+n))
else:
  print(k)


