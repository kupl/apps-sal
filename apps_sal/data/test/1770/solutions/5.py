t = int(input())
for _ in range(t):
  n, x, y, d = list(map(int, input().split()))
  ans = 1<<64
  if abs(x - y) % d == 0:
    ans = abs(x - y) // d
  if abs(1 - y) % d == 0:
    ans = min(ans, (abs(x - 1) + d - 1) // d + abs(1 - y) // d)
  if abs(n - y) % d == 0:
    ans = min(ans, (abs(x - n) + d - 1) // d + abs(n - y) // d)
  print(ans if ans != (1<<64) else -1)

