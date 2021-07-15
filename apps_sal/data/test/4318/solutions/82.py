n = int(input())
h = list(map(int,input().split()))
hi = h[0]
ans = 1
for i in range(1,n):
  if h[i] >= hi:
    ans += 1
    hi = h[i]
print(ans)
