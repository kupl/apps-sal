n,k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
h.sort()
ans = 0
for i in range(n-k):
  ans += h[i]
print(ans)
