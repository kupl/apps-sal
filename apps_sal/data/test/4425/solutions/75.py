n, k = map(int, input().split())
ans = 0
for i in range(1, n+1):
  cnt = 1
  while i < k:
    i *= 2
    cnt /= 2
  ans += cnt
ans /= n
print(ans)
