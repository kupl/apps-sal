n = int(input())

ans = (n+2)*(n+1)*n//6

for i in range(n-1):
  v, w = map(int, input().split())
  if v > w:
    v, w = w, v
  ans -= v*(n-w+1)
print(ans)
