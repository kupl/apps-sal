n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]

max_l, min_r = 0, float("inf")
for i in range(m):
  max_l = max(s[i][0], max_l)
  min_r = min(s[i][1], min_r)
  
print(max(min_r - max_l + 1, 0))
