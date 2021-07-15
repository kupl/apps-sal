N, T = map(int, input().split())
ans = 1001
for i in range(N):
  c, t = map(int, input().split())
  if t <= T:
    ans = min(ans, c)
print(ans) if ans < 1001 else print("TLE")

