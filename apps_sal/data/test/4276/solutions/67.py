n,t = map(int,input().split())
ans = 10**9
l = []
for i in range(n):
  l.append(list(map(int,input().split())))
for i in range(n):
  if l[i][1] <= t:
    ans = min(l[i][0],ans)
if ans == 10**9:
  print("TLE")
else:
  print(ans)
