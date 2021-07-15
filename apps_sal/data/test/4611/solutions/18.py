N = int(input())
t, x, y = 0, 0, 0
ans = "Yes"

for i in range(N):
  nt, nx, ny = map(int,input().split())
  if ((nt - t) - abs(nx - x) - abs(ny - y))%2 != 0 or abs(nx - x) + abs(ny - y) > (nt - t):
    ans = "No"
    break
  else:
    t = nt
    x = nx
    y = ny

print(ans)
