n, T = list(map(int, input().split()))
CT = [list(map(int, input().split())) for _ in range(n)]

ans = 1001
for c, t in CT:
    if t > T: continue
    ans = min(ans, c)
if ans == 1001:
  ans = "TLE"
print(ans)

