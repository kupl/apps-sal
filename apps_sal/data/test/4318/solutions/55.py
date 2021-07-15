n = int(input())
h = list(map(int,input().split()))
ans = 1
hi = h[0]
for i in range(1,n):
  if h[i] >= hi:
    ans += 1
    hi = h[i]
print(ans)
