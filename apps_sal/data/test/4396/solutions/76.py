N = int(input())

# やるだけ
ans = 0.0
for i in range(N):
  x, u = input().split()
  x = float(x)
  if u == 'JPY': ans += x
  if u == 'BTC': ans += 380000.0 * x
    
print(ans)
