N, K = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(N):
  if i == 0:
    n = 0
    k = 0
  else:
    n -= a[i-1]
    if n >= K:
      ans += N - k
      continue
    else:
      k += 1
  for j in range(k, N):
    n += a[j]
    if n >= K:
      k = j
      ans += N - j
      break
  else:
    k = j
print(ans)
