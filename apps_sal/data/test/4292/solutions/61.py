n, m = map(int, input().split())
p = list(map(int,input().split()))
p.sort()

ans = 0

for i in range(m):
  ans += p[i]
  
print(ans)
