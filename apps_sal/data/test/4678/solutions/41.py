N = int(input())
An = list(map(int, input().split()))
m = 0
ans = 0
for a in An:
  if a < m:
    ans += m - a
  else:
    m = a
print(ans)
