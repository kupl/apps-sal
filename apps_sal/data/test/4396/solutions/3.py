N = int(input())
btc_a = 380000.0
btc_b = btc_a / (10 ** 8)
ans = 0.0
for i in range(N):
  x, n = input().split()
  if n == "JPY":
    ans += int(x)
  else:
    a, b = map(int, x.split("."))
    ans += a * btc_a
    ans += b * btc_b
print(ans)
